from rest_framework.views import APIView
from rest_framework.response import Response
from django.core.files.storage import default_storage
from .models import JobListing
from .serializers import JobListingSerializer
from rest_framework import status
from rest_framework.pagination import PageNumberPagination
import os
from rest_framework.permissions import AllowAny
from django.db.models import Q

class StandardResultsSetPagination(PageNumberPagination):
    page_size = 20
    page_size_query_param = 'page_size'
    max_page_size = 100

class JobListingScrapeView(APIView):
    permission_classes = [AllowAny]
    
    def post(self, request):
        from .scrapers.linkedin import scrape_linkedin_jobs
        
        keywords = request.data.get('keywords', 'Data Scientist')
        location = request.data.get('location', 'Germany')
        category = request.data.get('category', None)
        
        try:
            results = scrape_linkedin_jobs(keywords, location, category)
            return Response({
                'message': f'Successfully scraped {len(results)} jobs',
                'jobs_count': len(results),
                'jobs': results
            }, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({
                'error': str(e)
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class JobListingListView(APIView):
    permission_classes = [AllowAny]
    pagination_class = StandardResultsSetPagination
    
    def get(self, request):
        jobs = JobListing.objects.all().order_by('-created_at')
        
        # Apply filters
        category = request.GET.get('category')
        location = request.GET.get('location')
        company = request.GET.get('company')
        search = request.GET.get('search')
        
        if category and category != 'all':
            jobs = jobs.filter(category=category)
        
        if location and location != 'all':
            jobs = jobs.filter(location__icontains=location)
        
        if company and company != 'all':
            jobs = jobs.filter(company__icontains=company)
        
        if search:
            jobs = jobs.filter(
                Q(title__icontains=search) | 
                Q(company__icontains=search) |
                Q(location__icontains=search) |
                Q(category__icontains=search)
            )
        
        # Add pagination
        paginator = self.pagination_class()
        page = paginator.paginate_queryset(jobs, request)
        
        if page is not None:
            serializer = JobListingSerializer(page, many=True)
            return paginator.get_paginated_response(serializer.data)
        
        serializer = JobListingSerializer(jobs, many=True)
        return Response(serializer.data)

class JobListingDetailView(APIView):
    permission_classes = [AllowAny]
    
    def get(self, request, pk):
        try:
            job = JobListing.objects.get(pk=pk)
            serializer = JobListingSerializer(job)
            return Response(serializer.data)
        except JobListing.DoesNotExist:
            return Response({'error': 'Job not found'}, status=404)

class FilterOptionsView(APIView):
    permission_classes = [AllowAny]
    
    def get(self, request):
        categories = [choice[0] for choice in JobListing.CATEGORY_CHOICES]
        locations = list(JobListing.objects.values_list('location', flat=True).distinct())
        companies = list(JobListing.objects.values_list('company', flat=True).distinct())
        
        return Response({
            'categories': [cat for cat in categories if cat],
            'locations': [loc for loc in locations if loc and loc != "N/A"],
            'companies': [comp for comp in companies if comp and comp != "N/A"],
        })
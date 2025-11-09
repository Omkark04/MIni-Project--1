from rest_framework.views import APIView
from rest_framework.response import Response
from django.core.files.storage import default_storage
from .models import JobListing, ScrapingSession
from .serializers import JobListingSerializer, ScrapingSessionSerializer, ScrapingRequestSerializer
from rest_framework import status
from rest_framework.pagination import PageNumberPagination
import os
from rest_framework.permissions import AllowAny
from django.db.models import Q
from django.utils import timezone
from django.db import transaction
import asyncio
import aiohttp
import time

class StandardResultsSetPagination(PageNumberPagination):
    page_size = 20
    page_size_query_param = 'page_size'
    max_page_size = 100

class ScrapingSessionView(APIView):
    permission_classes = [AllowAny]
    
    def get(self, request):
        sessions = ScrapingSession.objects.all().order_by('-created_at')
        serializer = ScrapingSessionSerializer(sessions, many=True)
        return Response(serializer.data)
    
    def delete(self, request, session_id):
        try:
            session = ScrapingSession.objects.get(id=session_id)
            jobs_count = session.jobs.count()
            
            # Delete associated image files before deleting jobs
            deleted_images_count = 0
            for job in session.jobs.all():
                if job.image_filename and default_storage.exists(f'job_images/{job.image_filename}'):
                    try:
                        default_storage.delete(f'job_images/{job.image_filename}')
                        deleted_images_count += 1
                    except Exception as e:
                        print(f"Error deleting image {job.image_filename}: {e}")
            
            # Delete the session (this will cascade delete all associated jobs due to CASCADE)
            session.delete()
            
            return Response({
                'message': f'Successfully deleted session, {jobs_count} jobs, and {deleted_images_count} image files'
            }, status=status.HTTP_200_OK)
            
        except ScrapingSession.DoesNotExist:
            return Response({'error': 'Session not found'}, status=404)
class JobListingScrapeView(APIView):
    permission_classes = [AllowAny]
    
    def post(self, request):
        from .scrapers.linkedin import scrape_linkedin_jobs
        
        serializer = ScrapingRequestSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        data = serializer.validated_data
        categories = data.get('categories', [])
        locations = data.get('locations', [])
        scrape_all_categories = data.get('scrape_all_categories', False)
        scrape_all_locations = data.get('scrape_all_locations', False)
        session_name = data.get('session_name', '')
        
        # Determine categories to scrape
        if scrape_all_categories:
            categories_to_scrape = [choice[0] for choice in JobListing.CATEGORY_CHOICES]
        else:
            categories_to_scrape = categories if categories else ['Data Scientist']  # Default
        
        # Determine locations to scrape
        LOCATIONS = [
            "United States", "Germany", "United Kingdom", "Canada", "Australia", "France",
            "India", "Japan", "Brazil", "Spain", "Italy", "Netherlands", "Switzerland",
            "Sweden", "Norway", "Denmark", "Finland", "Ireland", "Austria", "Belgium",
            "Portugal", "Poland", "Czech Republic", "Hungary", "Romania", "Greece",
            "Turkey", "Israel", "UAE", "Saudi Arabia", "South Africa", "Singapore",
            "Malaysia", "Thailand", "Vietnam", "Philippines", "South Korea", "Taiwan",
            "Hong Kong", "New Zealand", "Mexico", "Argentina", "Chile", "Colombia",
            "Peru", "Remote", "Hybrid", "On-site"
        ]
        
        if scrape_all_locations:
            locations_to_scrape = LOCATIONS
        else:
            locations_to_scrape = locations if locations else ['Germany']  # Default
        
        # Create scraping session
        session = ScrapingSession.objects.create(
            name=session_name or f"Scraping Session {timezone.now().strftime('%Y-%m-%d %H:%M')}",
            categories=categories_to_scrape,
            locations=locations_to_scrape
        )
        
        try:
            total_jobs = 0
            scraped_jobs = []
            
            # Scrape for each category and location combination
            for category in categories_to_scrape:
                for location in locations_to_scrape:
                    try:
                        # Pass the session to the scraper
                        results = scrape_linkedin_jobs(category, location, category, session)
                        total_jobs += len(results)
                        scraped_jobs.extend(results)
                        
                        print(f"✅ Scraped {len(results)} jobs for {category} in {location}")
                        
                    except Exception as e:
                        print(f"❌ Error scraping {category} in {location}: {str(e)}")
                        continue
            
            # Update session status
            session.total_jobs_scraped = total_jobs
            session.status = 'completed'
            session.completed_at = timezone.now()
            session.save()
            
            return Response({
                'message': f'Successfully scraped {total_jobs} jobs across {len(categories_to_scrape)} categories and {len(locations_to_scrape)} locations',
                'session_id': str(session.id),
                'jobs_count': total_jobs,
                'categories_scraped': categories_to_scrape,
                'locations_scraped': locations_to_scrape,
                'jobs': scraped_jobs[:10]  # Return first 10 jobs for preview
            }, status=status.HTTP_200_OK)
            
        except Exception as e:
            session.status = 'failed'
            session.save()
            return Response({
                'error': str(e),
                'session_id': str(session.id)
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
        session_id = request.GET.get('session_id')
        
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
        
        if session_id and session_id != 'all':
            jobs = jobs.filter(session_id=session_id)
        
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
        sessions = list(ScrapingSession.objects.values_list('id', 'name', 'created_at'))
        
        session_options = [{'id': 'all', 'name': 'All Sessions'}] + [
            {'id': str(session[0]), 'name': f"{session[1]} ({session[2].strftime('%Y-%m-%d')})"}
            for session in sessions
        ]
        
        return Response({
            'categories': [cat for cat in categories if cat],
            'locations': [loc for loc in locations if loc and loc != "N/A"],
            'companies': [comp for comp in companies if comp and comp != "N/A"],
            'sessions': session_options,
        })
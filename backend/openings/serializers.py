from rest_framework import serializers
from .models import JobListing, ScrapingSession

class JobListingSerializer(serializers.ModelSerializer):
    session_id = serializers.UUIDField(source='session.id', read_only=True, allow_null=True)
    session_name = serializers.CharField(source='session.name', read_only=True, allow_null=True)
    
    class Meta:
        model = JobListing
        fields = '__all__'

class ScrapingSessionSerializer(serializers.ModelSerializer):
    jobs_count = serializers.IntegerField(source='jobs.count', read_only=True)
    
    class Meta:
        model = ScrapingSession
        fields = '__all__'

class ScrapingRequestSerializer(serializers.Serializer):
    categories = serializers.ListField(
        child=serializers.CharField(max_length=50),
        required=False,
        default=[]
    )
    locations = serializers.ListField(
        child=serializers.CharField(max_length=100),
        required=False,
        default=[]
    )
    scrape_all_categories = serializers.BooleanField(default=False)
    scrape_all_locations = serializers.BooleanField(default=False)
    session_name = serializers.CharField(max_length=255, required=False, allow_blank=True)
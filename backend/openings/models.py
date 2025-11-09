from django.db import models
from django.utils import timezone
import uuid

class ScrapingSession(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255, blank=True)
    categories = models.JSONField(default=list)
    locations = models.JSONField(default=list)
    total_jobs_scraped = models.IntegerField(default=0)
    created_at = models.DateTimeField(default=timezone.now)
    completed_at = models.DateTimeField(null=True, blank=True)
    status = models.CharField(
        max_length=20,
        choices=[
            ('running', 'Running'),
            ('completed', 'Completed'),
            ('failed', 'Failed'),
        ],
        default='running'
    )
    
    class Meta:
        db_table = 'scraping_sessions'
        ordering = ['-created_at']
    
    def __str__(self):
        return f"Session {self.id} - {self.created_at.strftime('%Y-%m-%d %H:%M')}"

class JobListing(models.Model):
    CATEGORY_CHOICES = [
        ("Advocate", "Advocate"),
        ("Arts", "Arts"),
        ("Automation Testing", "Automation Testing"),
        ("BlockChain", "BlockChain"),
        ("Business Analyst", "Business Analyst"),
        ("Civil Engineer", "Civil Engineer"),
        ("Data Science", "Data Science"),
        ("Database", "Database"),
        ("DevOps", "DevOps"),
        (".Net", ".Net"),
        ("ETL", "ETL"),
        ("Electrical", "Electrical"),
        ("HR", "HR"),
        ("Hadoop", "Hadoop"),
        ("Health and Fitness", "Health and Fitness"),
        ("Java", "Java"),
        ("Mechanical", "Mechanical"),
        ("Network", "Network"),
        ("Operations", "Operations"),
        ("PMO", "PMO"),
        ("Python", "Python"),
        ("SAP", "SAP"),
        ("Sales", "Sales"),
        ("Testing", "Testing"),
        ("Web Design", "Web Design"),
    ]
    
    session = models.ForeignKey(ScrapingSession, on_delete=models.CASCADE, related_name='jobs', null=True, blank=True)
    title = models.CharField(max_length=255)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, null=True, blank=True)
    company = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    date_posted = models.CharField(max_length=100)
    job_link = models.URLField(max_length=500)
    image_url = models.URLField(max_length=500, null=True, blank=True)
    image_filename = models.CharField(max_length=255, null=True, blank=True)
    created_at = models.DateTimeField(default=timezone.now)
    
    class Meta:
        db_table = 'job_listings'
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.title} at {self.company}"
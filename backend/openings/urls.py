from django.urls import path
from .views import JobListingScrapeView, JobListingListView, JobListingDetailView, FilterOptionsView

urlpatterns = [
    path("scrape_jobs/", JobListingScrapeView.as_view(), name='scrape-jobs'),
    path("", JobListingListView.as_view(), name='job-list'),
    path("<int:pk>/", JobListingDetailView.as_view(), name='job-detail'),
    path("<int:pk>/get_image/", JobListingDetailView.as_view(), name='job-image'),
    path("filter_options/", FilterOptionsView.as_view(), name='filter-options'),
]
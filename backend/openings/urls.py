from django.urls import path
from .views import (
    JobListingScrapeView, 
    JobListingListView, 
    JobListingDetailView, 
    FilterOptionsView,
    ScrapingSessionView,
    JobCategory,
    LoadMore
)

urlpatterns = [
    path("scrape_jobs/", JobListingScrapeView.as_view(), name='scrape-jobs'),
    path("sessions/", ScrapingSessionView.as_view(), name='scraping-sessions'),
    path("sessions/<uuid:session_id>/", ScrapingSessionView.as_view(), name='scraping-session-detail'),
    path("", JobListingListView.as_view(), name='job-list'),
    path("<int:pk>/", JobListingDetailView.as_view(), name='job-detail'),
    path("<int:pk>/get_image/", JobListingDetailView.as_view(), name='job-image'),
    path("filter_options/", FilterOptionsView.as_view(), name='filter-options'),
    path('category/<str:category>', JobCategory.as_view(), name='category'),
    path('category/loadmore', LoadMore.as_view(), name='loadmore')
]
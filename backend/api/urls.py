from django.urls import path, include
from .views import Rform, AdminVerify

urlpatterns = [
    path("rform-data/", Rform.as_view(), name="rform"),
    path('adminverify/', AdminVerify.as_view(), name='adminverify')
]
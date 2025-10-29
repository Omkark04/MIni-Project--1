from django.urls import path, include
from .views import Rform

urlpatterns = [
    path("rform-data/", Rform.as_view(), name="rform")
]
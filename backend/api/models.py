from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import uuid

class UserRegisterData(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    full_name = models.CharField(max_length=40)
    email = models.EmailField(max_length=50, unique=True)
    mobile = models.CharField(max_length=16)
    dob = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.full_name} ({self.user.username})"
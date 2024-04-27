from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class ServiceRequest(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    request_type = models.CharField(max_length=100)
    details = models.TextField()
    attachment = models.FileField(upload_to='attachments/')
    status = models.CharField(max_length=50, default='Pending')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class user(models.Model):
    user_id = models.AutoField(primary_key=True)
    name=models.CharField(max_length=30)
    email=models.EmailField()
    password=models.CharField(max_length=30)
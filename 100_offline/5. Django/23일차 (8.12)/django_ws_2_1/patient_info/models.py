from django.db import models

# Create your models here.
class Patient(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    birth_date = models.DateField()
    email = models.TextField()
    phone_number = models.CharField(max_length=15)
    created_at = models.DateField(auto_now_add=True)
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinLengthValidator

class Address(models.Model):
    line1 = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    pincode = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.line1}, {self.city}, {self.state} - {self.pincode}"

class CustomUser(AbstractUser):
    USER_TYPE_CHOICES = (
        ('P', 'Patient'),
        ('D', 'Doctor'),
    )
    
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    profile_picture = models.ImageField(upload_to='profile_pics/', null=True, blank=True)
    user_type = models.CharField(max_length=1, choices=USER_TYPE_CHOICES)
    address = models.OneToOneField(Address, on_delete=models.CASCADE, null=True)
    email = models.EmailField(unique=True)

    def __str__(self):
        return f"{self.username} ({self.get_user_type_display()})"
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Registration(models.Model):
    FirstName = models.CharField(max_length=255)
    LastName = models.CharField(max_length=255)
    Image =  models.ImageField(upload_to='item_images',blank=True,null=True)

    def __str__(self):
        return self.FirstName
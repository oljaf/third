from django.db import models
from phonenumber_field.modelfields import PhoneNumberField 
from .validators import file_size
# Create your models here.
class Video(models.Model):
    caption=models.CharField(max_length=100)
    video=models.FileField(upload_to="video",validators=[file_size])
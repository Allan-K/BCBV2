from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone


class CustomUser(AbstractUser):
    pass
    # add additional fields in here

    def __str__(self):
        return self.username
    
class Songs(models.Model):
    title = models.CharField(max_length=50, null=True, blank=True, unique=True)
    description = models.TextField(blank=True)
    is_set = models.BooleanField(default=False)
    file = models.FileField(upload_to="songs/")

    class Meta:
        ordering = ['id']

    def __str__(self):
        return str(self.title)
    
    def delete(self):
        self.file.delete()
        super().delete()
    
class News(models.Model):
    heading = models.CharField(max_length=250)
    content_text = models.TextField(blank=True)
    image_file= models.ImageField(upload_to="images/")
    article_created_at = models.DateTimeField(default=timezone.now)
    
    class Meta:
        ordering =['-article_created_at']

    def __str__(self):
        return str(self.heading)
    
    def delete(self):
        self.image_file.delete()
        super().delete()
    
class Gallery(models.Model):
    heading = models.CharField(max_length=250)
    content_text = models.TextField(blank=True)
    image_file= models.ImageField(upload_to="images/gallery")
    article_created_at = models.DateTimeField(default=timezone.now)
    
    class Meta:
        ordering =['-article_created_at']

    def __str__(self):
        return str(self.heading)
    
    def delete(self):
        self.image_file.delete()
        super().delete()
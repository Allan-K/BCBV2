from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone


class CustomUser(AbstractUser):
    moderator = models.BooleanField(max_length=5, null=True, blank=True, default=False)
    # add additional fields in here

    def __str__(self):
        return self.username
    
class Songs(models.Model):
    TUNETYPE = (
        (1, 'N/A'),
        (2, 'Jig'),
        (3, 'Reel'),
        (4, 'Polka'),
        (5, 'Listening_Tune')
    )
    
    title = models.CharField(max_length=50, null=True, blank=True, unique=True)
    description = models.TextField(blank=True)
    tune_type = models.IntegerField(choices=TUNETYPE, default=1, blank=True, null=True)
    is_set = models.BooleanField(default=False, blank=True, null=True)
    file = models.FileField(upload_to="songs/")
    moderated = models.BooleanField(default=False, blank=True, null=True)

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

class Links(models.Model):
    link_name = models.URLField()
    description = models.TextField(blank=True)

    class Meta:
        ordering=['link_name']

class Documents(models.Model):
    heading = models.CharField(max_length=250)
    text = models.TextField(blank=True)
    doc_file= models.FileField(upload_to="documents/")
    article_created_at = models.DateTimeField(default=timezone.now)
    
    class Meta:
        ordering =['-article_created_at']

    def __str__(self):
        return str(self.heading)
    
    def delete(self):
        self.image_file.delete()
        super().delete()
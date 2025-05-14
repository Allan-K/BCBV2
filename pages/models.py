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
        ('N/A', 'N/A'),
        ('Jig', 'Jig'),
        ('Reel', 'Reel'),
        ('Polka', 'Polka'),
        ('Listening Tune', 'Listening_Tune')
    )
    SET = (
        ('0', 'No'),
        ('1', 'Yes')
    )

    MOD = (
        ('No', 'No'),
        ('Yes', 'Yes')
    )
    
    title = models.CharField(max_length=50, null=True, blank=True, unique=True)
    description = models.TextField(blank=True)
    tune_type = models.CharField(max_length=25, choices=TUNETYPE)
    is_set = models.CharField(max_length=5, choices=SET, default=False, blank=True, null=True)
    file = models.FileField(upload_to="songs/")
    moderated = models.CharField(max_length=5, choices=MOD, default=False, blank=True, null=True)


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
        self.doc_file.delete()
        super().delete()


class Set(models.Model):
    setTitle = models.CharField(max_length=50, null=True, blank=True, unique=True)
    setDate = models.DateField(default=timezone.now)

    class Meta:
        ordering = ['-setDate']
    def __str__(self):
        return str(self.setTitle)
    
class SetList(models.Model):
    set = models.ForeignKey(Set, on_delete=models.CASCADE)
    song = models.ForeignKey(Songs, on_delete=models.CASCADE)
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['order']
    def __str__(self):
        return str(self.set) + " - " + str(self.song)
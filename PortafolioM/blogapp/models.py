from django.db import models
from django.utils import timezone

class Blog(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='blog_images/')
    date_posted = models.DateTimeField(default=timezone.now)
    github_url = models.URLField()

    def __str__(self):
        return self.title

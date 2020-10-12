from django.conf import settings
from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class Likes(models.Model):
     '''いいね'''
     articles = models.ForeignKey('Post', on_delete=models.CASCADE)
     user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
     created_at = models.DateTimeField(auto_now_add=True)

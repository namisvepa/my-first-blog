from django.db import models
from django.utils import timezone

# Create your models here.

class Post(models.Model):
    """
    My class description
    """
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title  = models.CharField(max_length=200)
    text   = models.TextField()
    created_date = models.DateTimeField(blank=True, null=True)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        """
        My comments to class method
        """
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
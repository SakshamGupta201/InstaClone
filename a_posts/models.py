from django.db import models
import uuid


class Post(models.Model):
    __tablename__ = "posts"
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    artist = models.CharField(max_length=100, blank=True, null=True)
    url = models.URLField(max_length=200, blank=True, null=True)
    title = models.CharField(max_length=100)
    image = models.URLField(max_length=200, blank=True)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-created_at']
        verbose_name = "Post"

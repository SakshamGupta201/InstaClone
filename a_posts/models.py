from django.db import models
import uuid
from django.template.defaultfilters import slugify

class Post(models.Model):
    __tablename__ = "posts"
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    artist = models.CharField(max_length=100, blank=True, null=True)
    url = models.URLField(max_length=200, blank=True, null=True)
    title = models.CharField(max_length=100)
    image = models.URLField(max_length=200, blank=True)
    content = models.TextField()
    tags = models.ManyToManyField("Tag", related_name="posts")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Post"


class Tag(models.Model):
    __tablename__ = "tags"
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, unique=True, blank=True)

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    class Meta:
        ordering = ["name"]
        verbose_name = "Tag"

from django.db import models
from authy.models import User
import uuid

# Create your models here.

class Topic(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    title = models.CharField(max_length=100, null=True, blank=True)
    
    class Meta:
        verbose_name_plural = 'Topic'
    
    def __str__(self):
        return self.title


class Post(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    heading = models.CharField(max_length=200, null=True, blank=True)
    body = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to="post-media")
    no_of_liked_post = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name_plural = 'Post'
        ordering = ['-created_at', '-updated_at']
        
       
        
    def __str__(self):
        return self.heading    
    
    
class Comment(models.Model):
    id = models.UUIDField( primary_key=True, default=uuid.uuid4 )
    sender  = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    body = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name_plural = 'Comment'
        ordering = ['-created_at', '-updated_at']
        
    
    def __str__(self):
        return f'{self.sender} : {self.body[:20]}'
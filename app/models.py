from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Post(models.Model):
    title=models.CharField(max_length=100)
    description=models.TextField(max_length=400)
    img=models.ImageField(upload_to='Post',blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
    created_by=models.ForeignKey(User,on_delete=models.CASCADE,null=True)

    def __str__(self):
        return self.title




class Comment(models.Model):
    post=models.ForeignKey(Post,on_delete=models.CASCADE,related_name='comments')
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    text=models.TextField(max_length=400)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text
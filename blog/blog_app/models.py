from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
import uuid

class Post(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    title=models.CharField(max_length=100)
    slug = models.SlugField(unique=True, blank=True)
    content=models.TextField()
    cover_image=models.ImageField(upload_to='cover_images/',null=True,blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)


    def save(self,*args,**kwargs):
        if not self.slug:
            self.slug=slugify(self.title)

            while Post.objects.filter(slug=self.slug).exists():
                self.slug=f'{slugify(self.title)}-{uuid.uuid4().hex[:6]}'
                

        super().save(*args,**kwargs)

    def __str__(self):
        return self.title
class Follow(models.Model):
    follower=models.ForeignKey(User,related_name='follower',on_delete=models.CASCADE)
    following=models.ForeignKey(User,related_name='following',on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)

    class meta:
        unique_together=('follower','following')


    def __str__(self):
        return f'{self.follower.username} follower {self.following.username} following'

# Create your models here.


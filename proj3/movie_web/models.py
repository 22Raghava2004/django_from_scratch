from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Movies(models.Model):
    title=models.CharField(max_length=100)
    description=models.TextField()
    image=models.ImageField(upload_to='posters/')
    video=models.FileField(upload_to='videos/')
    genre=models.CharField(max_length=50)
    uploaded_by=models.ForeignKey(User,on_delete=models.CASCADE)
    uploaded_at=models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title

class Watchlist(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    movie=models.ForeignKey(Movies,on_delete=models.CASCADE)
    added_on =models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together=('user','movie')#<-------- this prevent duplicate entries


    def __str__(self):
        return f'{self.user.username} - {self.movie.title}'
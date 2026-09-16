from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Task(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    id=models.AutoField(primary_key=True)
    title=models.CharField(max_length=200)
    description=models.TextField()
    image=models.ImageField(upload_to='images/',null=True,blank=True)
    completed=models.BooleanField(default=False)
    
    completed_on=models.DateTimeField(auto_now_add=True,null=True,blank=True)

    def __str__(self):
        return self.title


from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    user=models.OneToOneField(User,null=True, on_delete=models.CASCADE)
    title = models.TextField()
    cover = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title
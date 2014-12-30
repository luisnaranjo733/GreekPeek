from django.db import models


class Chapter(models.Model):
    name = models.CharField(max_length=200)
    nickName = models.CharField(max_length=50)
    size = models.IntegerField(default=0)
    bio = models.TextField()
    
    def __str__(self):
        return self.nickName
        

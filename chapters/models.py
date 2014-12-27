from django.db import models


class Chapter(models.Model):
    chapter_name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.chapter_name

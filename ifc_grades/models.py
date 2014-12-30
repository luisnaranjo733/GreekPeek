from django.db import models

from chapters.models import Chapter

class GradeReport(models.Model):
    choices = (
        ('Fall', 'Fall'),
        ('Winter', 'Winter'),
        ('Spring', 'Spring'),
    )

    chapter = models.ForeignKey(Chapter)
    quarter = models.CharField(max_length=10, choices=choices) # Fall, Winter, or Spring
    year = models.IntegerField()
    
    cumulative_gpa = models.DecimalField(max_digits=3, decimal_places=2)
    new_member_gpa = models.DecimalField(max_digits=3, decimal_places=2)
    submitted_chapter_size = models.IntegerField()
    students_on_deans_list = models.IntegerField()
    
    def __str__(self):
        return '%s grades of %s %d' % (self.chapter, self.quarter, self.year)

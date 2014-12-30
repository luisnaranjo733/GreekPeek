from django.db import models

from ifc_grades.models import GradeReport

class Chapter(models.Model):
    name = models.CharField(max_length=200)
    nickName = models.CharField(max_length=50)
    size = models.IntegerField(default=0)
    bio = models.TextField()
    
    def __str__(self):
        return self.nickName
        
    def get_recent_grade_reports(self, number_of_reports=3):
        '''Returns a list of the most recent grade reports'''
        pass
        
    def get_last_grade_report(self):
        pass
        

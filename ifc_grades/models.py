from django.db import models


class GradeReport(models.Model):
    chapter = models.ForeignKey('chapters.Chapter')
    day_in_that_quarter = models.DateField()
    
    cumulative_gpa = models.DecimalField(max_digits=3, decimal_places=2)
    new_member_gpa = models.DecimalField(max_digits=3, decimal_places=2)
    submitted_chapter_size = models.IntegerField()
    students_on_deans_list = models.IntegerField()
    
    def __str__(self):
        key = (self.chapter,
            self.get_quarter(),
            self.day_in_that_quarter.year
        )
        return '%s grades of %s %d' % key
        
    def get_quarter(self):
        '''Tells what quarter grade report is from.'''
        day = self.day_in_that_quarter.timetuple().tm_yday

        # "day of year" ranges for the northern hemisphere
        spring = range(80, 172)
        summer = range(172, 264)
        fall = range(264, 355)
        # winter = everything else

        if day in spring:
            season = 'Spring'
        elif day in summer: # This probably shouldn't be here
            season = 'Summer'
        elif day in fall:
            season = 'Fall'
        else:
            season = 'Winter'
        return season

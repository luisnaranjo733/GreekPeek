from django.db import models

from GreekPeek import settings

from custom_user.models import AbstractEmailUser

#from django.contrib.auth import get_user_model
#user = get_user_model().get(email="user@example.com")

class User(AbstractEmailUser):
    """
    Example of an EmailUser with a new field date_of_birth
    """
    firstName = models.CharField(max_length=80, null=True)
    lastName = models.CharField(max_length=80, null=True)   

    def __str__(self):
        name = self.firstName
        if self.firstName and self.lastName:
            name += " " + self.lastName
        elif not self.firstName and self.lastName:
            name = lastName
        return name or 'NAME NOT DEFINED'

    def isRushChair(self):
        for chair in RushChair.objects.all():
            if chair.user == self:
                return True

        return False

    def isRecruit(self):
        for person in Recruit.objects.all():
            if person.user == self:
                return True

        return False


class Recruit(models.Model):
    date_of_birth = models.DateField(null=True, blank=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    grade = models.CharField(max_length=80, null=True, blank=True)
    phone = models.CharField(max_length=12, null=True, blank=True)
    major = models.CharField(max_length=80, null=True, blank=True)
    bio = models.TextField(null=True, blank=True)  
    houses = models.ManyToManyField('Chapter', blank=True)

    def __str__(self):
        return str(self.user)

    def subscribe(self, chapter):
        if chapter not in self.houses.all():
            self.houses.add(chapter)
            self.save()

    def unsubscribe(self, chapter):
        if chapter in self.houses.all():
            self.houses.remove(chapter)
            self.save()

    def getHouses(self):
        return self.houses.all()


class Chapter(models.Model):
    college = models.CharField(max_length=80, null=True)
    name = models.CharField(max_length=80, null=True)
    bio = models.TextField(null=True)

    def __str__(self):
        return self.name

class RushChair(models.Model):
    chapter = models.ForeignKey(Chapter)
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    phone = models.CharField(max_length=12, null=True, blank=True)

    def __str__(self):
        return '%s of %s' % (user, chapter)



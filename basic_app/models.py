from django.db import models
from django.forms import CharField
from django.core.urlresolvers import reverse

# Create your models here.
class School(models.model):
    name = models.CharField(max_length=256)
    principal = models.CharField(max_length=256)
    location = models.CharField(max_length=256)

    def __str__(self):
        return self.name

    def get_absolute_url(self):

class Student(models.Model):
    name = CharField(max_length=256)
    age = models.PositiveBigIntegerField()
    School = models.ForeignKey(School, related_name= 'students')


    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("basic_app:detail",kwargs={'pk':self.pk})

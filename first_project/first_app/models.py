from django.db import models

# Create your models here.
class Topic(models.Models):
    top_name = models.CharField(max_length=264,unique=True)

    def __str__(self):
        return self.top_name

class Webpage(models.Model):
    topic = models.FrorginKey(Topic)
    name = models.CharField(max_length=264,unique=True)
    path = models.URLField(unique=True)


    def __str__(self):
        return self.name

class AccessRecord(models.Model):
    name = models.ForeignKey(Webpage)
    date = models.DataField()

    def __str__(self):
        return str(self.date)


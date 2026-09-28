from django.db import models

class Organizer(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()


class Event(models.model):
    STATUS_CHOICES = [
        ('UPCOMING','upcoming'),
        ('ONGOING','Ongoing'),
        ('COMPLETED','Completed')
        ('CANCELLED','Cancelled')
    ]

    title = models.CharField(max_length=255)
    description = models.TextField

    status = models.CharField(max_length=20,choices = STATUS_CHOICES)
    organizer = models.ForeignKey(Organizer,on_delete = models.CASCADE)
    venue = models.ForeignKey('Venue ',on_delete = models.PROTECT )
    atendee = models.ManyToManyField('Atendee')

class Venue(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)

class Atendee(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()


# Create your models here.

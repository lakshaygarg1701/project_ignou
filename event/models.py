from django.db import models

# Create your models here.
from django.utils import timezone
from datetime import date

Category=(
    ('E-Sports', "E-Sports"),
    ('Sports', "Sports"),
    ('Technical', "Technical"),
    ('Cultural', "Cultural"),
    ('Others', "Others"),
)

Dept=(
    ('CS','CS'),
    ('BBA','BBA'),
    ('B.Com.','B.Com.'),
    ('B.Ed.','B.Ed.')
)

class Post(models.Model):
    dept = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    date_added = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class Event(models.Model):
    id1 = models.IntegerField(primary_key=True)
    name = models.TextField()
    email = models.TextField(blank=True, null=True)
    body = models.TextField()
    date = models.DateTimeField()
    venue = models.TextField()
    link = models.TextField()
    contact = models.TextField()
    category = models.TextField(blank=True, null=True)
    dept = models.TextField(blank=True, null=True)
    img = models.TextField()
    added_on = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'event'

class EventDetail(models.Model):
    id1 = models.IntegerField()
    email = models.EmailField()

    def publish(self):
        self.save()

    class Meta:
        db_table = 'event_detail'

class EventRep(models.Model):
    id1 = models.IntegerField(primary_key=True)
    name = models.TextField()
    email = models.TextField(blank=True, null=True)
    report = models.TextField()
    date = models.DateTimeField()
    contact = models.TextField()
    category = models.TextField(blank=True, null=True)
    dept = models.TextField(blank=True, null=True)
    img = models.TextField(blank=True, null=True)
    added_on = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'event_rep'

class EventFdbck(models.Model):
    id1 = models.IntegerField(primary_key=True)
    name = models.TextField()
    email = models.TextField(blank=True, null=True)
    feedback = models.TextField()
    date = models.DateTimeField()
    added_on = models.DateTimeField(blank=True, null=True)
    uname = models.TextField()

    class Meta:
        managed = False
        db_table = 'event_fdbck'

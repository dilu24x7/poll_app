from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Poll(models.Model):
    """Poll model for particular poll with fields question, poll type(single or multiple)
    author and publishing date"""
    poll_question = models.CharField(max_length=300)
    poll_type = models.BooleanField()
    poll_creator = models.ForeignKey(User)
    poll_pub_date = models.DateField()

class Choice(models.Model):
    """Choice model for storing the choices with field poll(foreign key of poll model)
    choice and votes"""
    poll = models.ForeignKey(Poll)
    poll_choice = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

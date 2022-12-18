from django.db import models
from datetime import datetime

# Create your models here.
class Chat(models.Model):
    HUMAN = 'H'
    BOT = 'B'
    USERS= [(HUMAN,'human'), (BOT, 'bot')]
    date_created = models.DateField(auto_now_add=True)
    user = models.CharField(
        max_length=1,
        choices=USERS,
        default=HUMAN,
    )
    message = models.TextField()
    
    
class Activity(models.Model):

    date_created = models.DateTimeField(auto_now_add=True)

    title = models.CharField(max_length=70)
    description = models.TextField()
    
    def __str__(self):
        return self.date_created+ " | "+ self.mood

    

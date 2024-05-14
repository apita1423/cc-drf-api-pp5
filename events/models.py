from django.db import models
from django.contrib.auth.models import User

class Event(models.Model):
    """
    Events model
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField(max_length=500, null=False, blank=False)
    date = models.DateField(null=True, blank=True)
    time = models.TimeField(null=True, blank=True)
    city = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    event_url = models.URLField('Event Url', max_length=355, blank=True)
    audience = models.TextField(max_length=300, blank=False)
    price = models.IntegerField(null=True, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        """
        Order events by date
        """
        ordering = ['created_on']
    
    def __str__(self):
        return f'Event: {self.title} | Date: {self.date}'
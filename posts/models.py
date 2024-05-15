from django.db import models
from django.contrib.auth.models import User

# Code Credit: DRF API Walkthrough
# Modifications made to the image_filter_choices
class Post(models.Model):
    """
    Post model, related to 'owner', i.e. a User instance.
    Default image set so that we cal always reference image.url.
    """
    image_filter_choices = [
    ('galaxy', 'Galaxy'), 
    ('deep space', 'Deep Space'),
    ('sun', 'Sun'), 
    ('mercury', 'Mercury'),
    ('venus', 'Venus'), 
    ('earth', 'Earth'),
    ('mars', 'Mars'), 
    ('jupiter', 'Jupiter'),
    ('saturn', 'Saturn'), 
    ('uranus', 'Uranus'),
    ('neptune', 'Neptune'), 
    ('aurora borealis', 'Aurora Borealis'),
    ('citizen science', 'Citizen Science'), 
    ('astrophotography', 'Astrophotography'),
    ('art', 'Art'),
    ('deep space', 'Deep Space'),
    ('solar system', 'Solar System'),
    ('science fiction', 'Science Fiction'),
    ('telescope', 'Telescope'),
    ('spacecraft', 'Spacecraft'),
    ('missions', 'Missions'),
    ]
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    image = models.ImageField(
        upload_to='images/', default='../default_profile_cmtzmv',
        blank=True
    )
    image_filter = models.CharField(
        max_length=32, choices=image_filter_choices, default='normal'
    )

    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return f'{self.id} {self.title}'
    
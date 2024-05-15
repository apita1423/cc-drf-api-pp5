from django.db import models
from django.contrib.auth.models import User

class Chronicle(models.Model):
    """
    News Model
    """
    category_choices = [
        ('space news', 'Space News'),
        ('exploration', 'Exploration'),
        ('stargazing tips', 'Stargazing Tips'),
        ('education', 'Education'),
        ('space missions', 'Space Missions'),
        ('technology', 'Technology'),
        ('astronomy events', 'Astronomy Events'),
        ('science', 'Science'),
        ('planets', 'Planets'),
        ('solar system', 'Solar System'),
    ]
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    category = models.CharField(
        max_length=55,
        choices=category_choices, 
        default='space news'
    )
    author = models.CharField(max_length=255)
    published_on = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(
        upload_to='images/', 
        default='../default_post_w1mkqv',
        blank=True, 
    )
    image_copyright = models.CharField(max_length=255, blank=False)

    class Meta:
        """
        News display by date created.
        """
        ordering = ['-created_at']
    
    def __str__(self):
        return f'By: {self.author} | Published: {self.published_on}'
    
    
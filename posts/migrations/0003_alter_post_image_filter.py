# Generated by Django 5.0.6 on 2024-05-15 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_post_image_filter'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image_filter',
            field=models.CharField(choices=[('galaxy', 'Galaxy'), ('deep space', 'Deep Space'), ('sun', 'Sun'), ('mercury', 'Mercury'), ('venus', 'Venus'), ('earth', 'Earth'), ('mars', 'Mars'), ('jupiter', 'Jupiter'), ('saturn', 'Saturn'), ('uranus', 'Uranus'), ('neptune', 'Neptune'), ('aurora borealis', 'Aurora Borealis'), ('citizen science', 'Citizen Science'), ('astrophotography', 'Astrophotography'), ('art', 'Art'), ('deep space', 'Deep Space'), ('solar system', 'Solar System'), ('science fiction', 'Science Fiction'), ('telescope', 'Telescope'), ('spacecraft', 'Spacecraft'), ('missions', 'Missions')], default='normal', max_length=32),
        ),
    ]

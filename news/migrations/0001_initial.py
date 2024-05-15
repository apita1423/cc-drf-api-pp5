# Generated by Django 5.0.6 on 2024-05-15 15:11

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Chronicle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('category', models.CharField(choices=[('space news', 'Space News'), ('exploration', 'Exploration'), ('stargazing tips', 'Stargazing Tips'), ('education', 'Education'), ('space missions', 'Space Missions'), ('technology', 'Technology'), ('astronomy events', 'Astronomy Events'), ('science', 'Science'), ('planets', 'Planets'), ('solar system', 'Solar System')], default='space news', max_length=55)),
                ('author', models.CharField(max_length=255)),
                ('published_on', models.DateTimeField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('image', models.ImageField(blank=True, default='../default_post_w1mkqv', upload_to='images/')),
                ('image_copyright', models.CharField(max_length=255)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
    ]
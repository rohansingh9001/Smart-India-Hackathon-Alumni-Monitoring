from django.db import models
from django.contrib.auth.models import AbstractUser
from PIL import Image

COLLEGE_CHOICES = (
    ('FIRST', 'FIRST'),
    ('SECOND', 'SECOND'),
    ('THIRD', 'THIRD'),
    ('FOURTH', 'FOURTH'),
    ('FIFTH', 'FIFTH'),
    ('SIXTH', 'SIXTH'),
    ('SEVENTH', 'SEVENTH'),
    ('EIGHTH', 'EIGHTH'),
)


class User(AbstractUser):
    is_alumni = models.BooleanField(default=False)
    is_college = models.BooleanField(default=False)
    College = models.CharField(
        max_length=80,
        choices=COLLEGE_CHOICES,
        default="None"
        )
    About = models.TextField(max_length=200)
    Work = models.TextField(max_length=50)
    Year_Joined = models.CharField(max_length=4)
    Branch = models.CharField(max_length=50)
    Image = models.ImageField(
        upload_to='images',
        default='default/test.png'
        )
    Verified = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.Image.path)
        if img.height > 300 or img.width > 300:
            output_size = (150, 150)
            img.thumbnail(output_size)
            img.save(self.Image.path)

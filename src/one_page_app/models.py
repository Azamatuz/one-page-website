from django.db import models

# text alignment bootstrap class choices
TEXT_ALIGNMENT_CHOICES = [
    ('text-left', 'Left'),
    ('text-center', 'Center'),
    ('text-right', 'Right'),
]
# button color bootstrap class choices
BUTTON_COLOR_CHOICES = [
    ('btn-primary', 'Primary'),
    ('btn-secondary', 'Secondary'),
    ('btn-success', 'Success'),
    ('btn-danger', 'Danger'),
    ('btn-warning', 'Warning'),
    ('btn-info', 'Info'),
    ('btn-light', 'Light'),
    ('btn-dark', 'Dark'),
    ('btn-link', 'Link'),
]


# Create your models here.
class CarouselSlide(models.Model):
    image = models.ImageField(upload_to='carousel/')
    title = models.CharField(max_length=100)
    description = models.TextField(default='No description available')
    # text alignment bootstrap class from dropdown choices
    text_alignment = models.CharField(max_length=11, choices=TEXT_ALIGNMENT_CHOICES, default='text-left')
    button_text = models.CharField(max_length=100, default='Learn More')
    button_link = models.CharField(max_length=200, default='#')
    button_style = models.CharField(max_length=15, choices=BUTTON_COLOR_CHOICES, default='btn-primary')

    def __str__(self):
        return self.title

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(default='No description available')
    image = models.ImageField(upload_to='products/')
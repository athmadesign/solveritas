from django.db import models

# Create your models here.
class Slider(models.Model):
    title = models.CharField(max_length=200, blank=True, null=True)
    subtitle = models.CharField(max_length=300, blank=True, null=True)
    image = models.ImageField(upload_to='sliders/')
    order = models.PositiveIntegerField(default=0, help_text="Slide display order")
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title if self.title else f"Slide {self.id}"
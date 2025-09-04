from django.db import models

# Create your models here.


class Download(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    file = models.FileField(upload_to="downloads/")
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
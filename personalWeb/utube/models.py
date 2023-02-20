from django.db import models

# Create your models here.
class Video(models.Model):
    title = models.CharField(max_length=200)
    vid = models.FileField()

    def __str__(self):
        return self.title
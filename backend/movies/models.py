from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=200)
    video_file = models.FileField(upload_to='movies/')
    description = models.TextField()
    date_added = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title
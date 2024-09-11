from django.db import models

class Video(models.Model):
    title = models.CharField(max_length=100)
    video_file = models.FileField(upload_to='videos/')  # 'videos/' is the folder where videos will be stored in the media directory

    def __str__(self):
        return self.title
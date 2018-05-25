from django.db import models

class About(models.Model):
    title = models.CharField(max_length=125)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    thumb = models.ImageField(default='default.png', blank=True)


    def __str__(self):
        return self.title

    def snippet(self):
        return self.body[:200] + '...'

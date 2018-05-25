from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=125)
    slug = models.SlugField()
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    thumb = models.ImageField(default='default.png', blank=True)
    author = models.CharField(max_length=125, default='Patrick Gabbard')


    def __str__(self):
        return self.title

    def snippet(self):
        return self.body[:200] + '...'




    #add in thumbnail later
    #add in author later

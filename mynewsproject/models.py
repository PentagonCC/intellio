from django.db import models


class News(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    date = models.DateField()
    source = models.URLField()
    image_url = models.URLField()
    category = models.CharField(max_length=100)

    def __str__(self):
        return self.title

from django.db import models
from sorl.thumbnail import ImageField


class Post(models.Model):
    text = models.CharField(max_length=140, blank=False, null=False)
    image = ImageField()

    def __str__(self):
        return self.text

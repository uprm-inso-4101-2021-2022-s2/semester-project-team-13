from django.db import models

# Create your models here.


class Mod(models.Model):
    mod_title = models.CharField(max_length=200)
    mod_author = models.CharField(max_length=200)
    mod_source = models.CharField(max_length=200)
    mod_game = models.CharField(max_length=200)
    mod_description = models.TextField()

    def __str__(self):
        return self.mod_title


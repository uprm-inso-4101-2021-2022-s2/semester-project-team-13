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


class Discussion(models.Model):
    dis_title = models.CharField(max_length=200)
    dis_author = models.CharField(max_length=100, default="Guest")
    dis_mod = models.ForeignKey(Mod, blank=True, null=True, on_delete=models.CASCADE)
    dis_date = models.DateTimeField(auto_now=True, null=True)
    DIS_TYPES = [
        ('General', 'General'),
        ('Game', 'Game'),
        ('Mod', 'Mod'),
    ]
    dis_type = models.CharField(max_length=7, choices=DIS_TYPES)
    dis = models.TextField()

    def __str__(self):
        return self.dis_title


class Reply(models.Model):
    rep_parent = models.ForeignKey(Discussion, on_delete=models.CASCADE)
    rep_author = models.CharField(max_length=100, default='Guest')
    rep_title = models.CharField(max_length=200)
    rep_date = models.DateTimeField(auto_now=True, null=True)
    rep = models.TextField()

    def __str__(self):
        return self.rep_title


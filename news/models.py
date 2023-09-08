from django.db import models

# Create your models here.
class Essay(models.Model):
    author = models.CharField(max_length=150)
    title = models.CharField(max_length=150)
    body = models.TextField()
    isActive = models.BooleanField(default=True)
    cre_date = models.DateTimeField(auto_now_add=True) #autonowadd provides an unchangable date.
    up_date = models.DateTimeField(auto_now=True)
    pub_date = models.DateField()

    def __str__(self):
        return self.title
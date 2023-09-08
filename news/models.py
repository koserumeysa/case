from django.db import models

class Reporter(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    bio = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'{self.name} {self.surname}'
    

# Create your models here.
class Essay(models.Model):
    #If we delete a reporter, all the essays of that reporter will be deleted.
    author = models.ForeignKey(Reporter, on_delete=models.CASCADE, related_name='essays')
    title = models.CharField(max_length=150)
    body = models.TextField()
    isActive = models.BooleanField(default=True)
    cre_date = models.DateTimeField(auto_now_add=True) #autonowadd provides an unchangable date.
    up_date = models.DateTimeField(auto_now=True)
    pub_date = models.DateField()

    def __str__(self):
        return self.title
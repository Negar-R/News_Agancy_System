from django.db import models

# Create your models here.

class Author(models.Model):

    name = models.CharField(max_length = 50)

    def __str__(self):
        return self.name 
    

class News1(models.Model):

    text = models.CharField(max_length = 500)
    date = models.DateTimeField()
    reporter = models.ForeignKey(Author , on_delete = models.CASCADE)

    def __str__(self):
        return self.text
    
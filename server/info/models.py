from django.db import models

# Create your models here.
class DbImage(models.Model):
    image = models.ImageField(upload_to='images/')
    name = models.CharField(max_length=400)
    date_added = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name
    

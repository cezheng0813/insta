from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.TextField(blank = True, null= True)
    image = models.ImageField(upload_to= 'static/images/posts',
    blank = True,
    null = True)
    
    def __str__(self):
        return self.title
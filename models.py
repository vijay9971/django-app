from django.db import models

class BlogModel(models.Model):                                                                                                                                                                                                                                      
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images', blank=True)
    description = models.TextField()

    def __str__(self):                                                               
        return self.title



# Create your models here.

  

                                                                                                                                                                                                                                     







# Create your models here.

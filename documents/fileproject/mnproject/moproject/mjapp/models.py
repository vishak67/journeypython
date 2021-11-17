from django.db import models

# Create your models here.
class place(models.Model):
    name=models.CharField(max_length=250)
    img=models.ImageField(upload_to='pics')
    disc=models.CharField(max_length=300)
    def __str__(self):
        return self.name

class food(models.Model):
    nam = models.CharField(max_length=250)
    im = models.ImageField(upload_to='pics')
    dis = models.CharField(max_length=300)

    def __str__(self):
        return self.nam

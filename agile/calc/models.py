from django.db import models
class Destination(models.Model):
    Name=models.charField(max_length=100)
    img=models.Image.Field(upload_to='pic')
    desc=models.TextField()
    price=models.Integerfield
    offer=models.BooleanField(default=False)
# Create your models here.

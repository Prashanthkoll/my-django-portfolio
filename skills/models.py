from django.db import models

# Create your models here.
class Skills(models.Model):
    title=models.CharField(max_length=300)
    point=models.TextField()
    
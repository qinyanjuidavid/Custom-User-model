from django.db import models

class background(models.Model):
    image=models.ImageField(upload_to='picts')

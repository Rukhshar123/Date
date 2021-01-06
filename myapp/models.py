from django.db import models

class Register(models.Model):
    name = models.CharField(max_length=20)
    email =  models.EmailField()
    date = models.DateField(auto_now_add=False,auto_now=False,blank=False)
    time = models.TimeField(auto_now_add=False,auto_now=False,blank=False)

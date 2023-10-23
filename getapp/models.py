from django.db import models

# Create your models here.
class contactcls(models.Model):
    name=models.CharField(max_length=30)
    email=models.CharField(max_length=150)
    message=models.CharField(max_length=500)

    def __str__(self) -> str:
        return self.name

   
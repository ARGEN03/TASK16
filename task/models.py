from django.db import models

# Create your models here.
class PersonalData(models.Model):
    name = models.CharField(max_length=76)
    last_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=60)
    address = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name
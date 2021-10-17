from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
ROLE = [
    (1,'Admin'),
    (2,'Operario'),
]

class CustomsUser(AbstractUser):
    role = models.IntegerField(max_length=50,choices=ROLE,default=1)
    date_update = models.DateTimeField(auto_now=True)

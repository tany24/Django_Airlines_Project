from django.db import models

# Create your models here.
class UserInfo(models.Model):
    first_name = models.CharField(max_length=240)
    last_name = models.CharField(max_length=240)
    emailID = models.URLField(unique=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

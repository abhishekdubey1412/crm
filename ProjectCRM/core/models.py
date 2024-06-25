from django.db import models

# Create your models here.
class Records(models.Model):
    first_name = models.CharField(max_length=30)
    last_name  = models.CharField(max_length=30, null=True, blank=True)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    address =models.CharField(max_length=200)
    city = models.CharField(max_length=20, blank=True)
    state = models.CharField(max_length=20, blank=True)
    country = models.CharField(max_length=20, blank=True)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.first_name + " " + self.last_name
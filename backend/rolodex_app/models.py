from datetime import datetime
from django.db import models

class Contact(models.Model):
    first_name = models.CharField(max_length=50, null=False)
    last_name = models.CharField(max_length=50, null=False)
    address = models.CharField(max_length=100, null=True, default="N/A")
    city = models.CharField(max_length=35, null=True, default="N/A")
    state = models.CharField(max_length=2, null=True)
    zip = models.CharField(max_length=5, null=True, default="XXXXX")
    phone = models.CharField(max_length=12, null=True, default="XXX-XXX-XXXX")
    email = models.EmailField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

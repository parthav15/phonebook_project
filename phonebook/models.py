from django.db import models

from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)

    def __str__(self):
        return self.name

from django.db import models

# Create your models here.
class Customers(models.Model):
    name = models.CharField(max_length=20, null=True)
    email = models.CharField(max_length=20, null=True)
    subject = models.CharField(max_length=20, null=True)
    message = models.TextField(max_length=30, null=True)
    date = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.subject
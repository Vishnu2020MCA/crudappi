from django.db import models

class employees(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    address = models.TextField()
    phone = models.IntegerField()

    class Meta:
        db_table = "employe"

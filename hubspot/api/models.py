from django.db import models


class User(models.Model):
    first_name = models.CharField(max_length=20)
    second_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=50)

    def __str__(self):
        return self.email


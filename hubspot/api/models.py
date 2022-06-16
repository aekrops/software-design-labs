from django.db import models
from django.utils import timezone


class User(models.Model):
    first_name = models.CharField(max_length=25)
    second_name = models.CharField(max_length=25)
    email = models.EmailField(max_length=50)

    def __str__(self):
        return f'{self.first_name[0]}: {self.email}'


class Client(models.Model):
    email = models.EmailField(max_length=50)
    phone_number = models.CharField(max_length=13)

    def __str__(self):
        return self.email

    def set_phone_number(self, phone_number):
        if len(str(phone_number)) <= 12:
            self.phone_number = phone_number
            return True
        else:
            print("Wrong phone number!")
            return False


class Conversation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.pk}: {self.user} - {self.client}'


class Message(models.Model):
    conversation = models.ForeignKey(Conversation, on_delete=models.CASCADE)
    text = models.TextField(max_length=256)
    time = models.DateField(editable=False, default=timezone.now)

    def __str__(self):
        return f'{self.pk}: {self.text[:6]} \t\t {self.time}'

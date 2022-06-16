from django.contrib import admin
from .models import User, Client, Conversation, Message


admin.site.register(User)
admin.site.register(Client)
admin.site.register(Conversation)
admin.site.register(Message)

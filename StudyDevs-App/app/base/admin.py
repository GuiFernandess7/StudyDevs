from django.contrib import admin
from .models import Room, Topic, Message, MyUser

admin.site.register(Room)
admin.site.register(Topic)
admin.site.register(Message)
admin.site.register(MyUser)

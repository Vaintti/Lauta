from django.contrib import admin

from threads.models import Thread, Message

admin.site.register(Thread)
admin.site.register(Message)
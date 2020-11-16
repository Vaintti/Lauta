from uuid import uuid4

from django.db import models
from boards.models import Board


class Thread(models.Model):
    board = models.ForeignKey(Board, on_delete=models.CASCADE)
    uuid = models.TextField(default=str(uuid4().int), editable=False)

    def __str__(self):
        return self.uuid

    def last_message_created_at(self):
        return self.message_set.all().order_by('created_at')[0].created_at


class Message(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    thread = models.ForeignKey(Thread, on_delete=models.CASCADE)
    content = models.CharField(max_length=500)

    def __str__(self):
        return self.content

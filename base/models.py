import uuid
from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Topic(models.Model):

    name = models.CharField(max_length=200)

    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    def __str__(self) -> str:
        return self.name

class Room(models.Model):
    host = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    # 1 - many : room can have multiple topics if the topic is deleted the topic in room will be set to null
    # the null hase been added to allow database to be null at the faild topic
    topic = models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    # participants =
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    class Meta:
        ordering = ['-updated', '-created']

    def __str__(self) -> str:
        return str(self.name)

class Message(models.Model):
    # the CASCADE will help us example if the user is deleted all his message will be deleted
    # 1 -> many: the user can have multiple messages
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # 1 -> many: the room can have multiple messages
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    body = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    def __str__(self) -> str:
        return self.body[0:50]
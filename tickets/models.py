from django.db import models


class Player(models.Model):
    name = models.CharField(max_length=100)
    color = models.CharField(max_length=6)


class Session(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    finished_at = models.DateTimeField(null=True)


class Ticket(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    player = models.ForeignKey(Player, on_delete=models.CASCADE, related_name="tickets")
    session = models.ForeignKey(Session, on_delete=models.CASCADE, related_name="tickets")

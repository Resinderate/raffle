from django.db import models


class Player(models.Model):
    name = models.CharField(max_length=100)
    color = models.CharField(max_length=6)

    def __str__(self):
        return self.name


class Session(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    finished_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.name


class Ticket(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    player = models.ForeignKey(Player, on_delete=models.CASCADE, related_name="tickets")
    session = models.ForeignKey(Session, on_delete=models.CASCADE, related_name="tickets")

    def __str__(self):
        return f"{self.player.name} -- {self.session.name}"

from django.db import models
from django.contrib.auth.models import User


class Gameboard(models.Model):
    gameboard_name = models.CharField(max_length=200)
    gameboard_created_at = models.DateTimeField(auto_now_add=True)


class PlayerGameboard(models.Model):
    player_id = models.ForeignKey(User, on_delete=models.CASCADE)
    gameboard_id = models.ForeignKey(Gameboard, on_delete=models.CASCADE)

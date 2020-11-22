from django.db import models
from django.contrib.auth.models import User


class Gameboard(models.Model):
    gameboard_name = models.CharField(max_length=200)
    gameboard_created_at = models.DateTimeField(auto_now_add=True)
    gameboard_players = models.ManyToManyField(User, through='PlayerGameboard')

    def total_players(self):
        return self.gameboard_players.count()

    def __str__(self):
        return self.gameboard_name


class PlayerGameboard(models.Model):
    player_id = models.ForeignKey(User, on_delete=models.CASCADE)
    gameboard_id = models.ForeignKey(Gameboard, on_delete=models.CASCADE)

    def __str__(self):
        return self.gameboard_id.gameboard_name + " - " + str(self.player_id) + " - " + str(self.id)


class GamePiece(models.Model):
    piece_name = models.CharField(max_length=200)
    piece_pic = models.ImageField(upload_to='image/pieces/')

    def __str__(self):
        return str(self.piece_name)

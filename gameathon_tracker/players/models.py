from django.db import models
from django.contrib.auth.models import User
from gameboard.models import GamePiece


class Profile(models.Model):
    player = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    profile_pic = models.ImageField(null=True, blank=True, upload_to='img/profile/')
    profile_game_piece = models.ForeignKey(GamePiece, null=True, blank=True, on_delete=models.SET_NULL, related_name='piece')

    def __str__(self):
        return str(self.player)


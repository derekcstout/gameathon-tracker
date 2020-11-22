from django.contrib import admin
from .models import Gameboard, PlayerGameboard, GamePiece

admin.site.register(Gameboard)
admin.site.register(PlayerGameboard)
admin.site.register(GamePiece)

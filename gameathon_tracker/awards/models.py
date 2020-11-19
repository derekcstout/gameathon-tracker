from django.db import models
from django.urls import reverse

class Award(models.Model):
    player_gameboard_id = models.ForeignKey('gameboard.PlayerGameboard', on_delete=models.CASCADE)
    game_name = models.CharField(max_length=200)
    position = models.IntegerField()
    team_game = models.BooleanField()
    points_awarded = models.IntegerField()
    award_created_at = models.DateTimeField(auto_now_add=True)

    #this defines where to redirect after a form submit
    def get_absolute_url(self):
        return reverse('awards')




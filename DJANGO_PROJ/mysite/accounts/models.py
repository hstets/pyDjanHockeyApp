from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class PerkyPlayers(models.Model):
    id = models.IntegerField(primary_key=True)
    team = models.ForeignKey('PerkyTeams', models.DO_NOTHING)
    player_name = models.CharField(max_length=500)
    player_position = models.CharField(max_length=250)

    class Meta:
        db_table = 'perky_players'

class PerkyTeams(models.Model):
    id = models.IntegerField(primary_key=True)
    team_name = models.CharField(max_length=250)

    class Meta:
        db_table = 'perky_teams'

from django.shortcuts import render, HttpResponse
from accounts.models import PerkyPlayers, PerkyTeams
import psycopg2
import datetime


# Create your views here.
def home(request):

    # get current date and time for display
    current_perky_time = datetime.datetime.now()

    # Generate count for number of perky players
    num_players = PerkyPlayers.objects.all().count()
    num_teams = PerkyTeams.objects.all().count()
    perky_players = PerkyPlayers.objects.all()

    args = {
        'num_of_players': num_players,
        'num_of_teams': num_teams,
        'time_current': current_perky_time,
        'player_list': perky_players
    }


    # render the home.html page
    return render(request, 'accounts/home.html', args)

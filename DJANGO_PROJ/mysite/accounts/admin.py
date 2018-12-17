from django.contrib import admin
from accounts.models import PerkyPlayers, PerkyTeams

# Register your models here.
admin.site.register(PerkyPlayers)
admin.site.register(PerkyTeams)

from django.shortcuts import render

from django.views import generic

from .models import editTeam

from django.urls import reverse

# Create your views here.

def view(request):
    return render(template_name='team/view.html', request=request)

class editTeamView(generic.CreateView):
    model = editTeam
    template_name = 'team/editTeam.html'
    fields = ['team_name', 'wins', 'losses', 'players']
class teamInfoView(generic.ListView):
    model = editTeam
    template_name = 'team/teamInfo.html'
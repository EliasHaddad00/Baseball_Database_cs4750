from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from django.db.models import Q

from sluggers.models import Team, Match

from datetime import datetime

def view(request, team_id):
    context = {'team': Team.objects.get(team_id=team_id)}
    
    future_games = Match.objects.all().filter(Q(home_team=team_id)|Q(away_team=team_id)).filter(match_date__gt=datetime.now()).order_by('match_date')
    past_games = Match.objects.all().filter(Q(home_team=team_id)|Q(away_team=team_id)).filter(match_date__lte=datetime.now()).order_by('match_date')

    if len(future_games) > 0:
            context['next_game'] = future_games[0]
            context['upcoming_games'] = future_games[1:]

    if len(past_games) > 0:
        context['past_games'] = past_games

    return render(template_name='team/view.html', request=request, context=context)

@login_required
def edit(request, team_id):
    team = Team.objects.get(team_id=team_id)
    future_games = Match.objects.all().filter(Q(home_team=team_id)|Q(away_team=team_id)).filter(match_date__gt=datetime.now()).order_by('match_date')
    past_games = Match.objects.all().filter(Q(home_team=team_id)|Q(away_team=team_id)).filter(match_date__lte=datetime.now()).order_by('match_date')
    
    context = {}

    if request.method == 'GET':
        if len(future_games) > 0:
            context['next_game'] = future_games[0]
            context['upcoming_games'] = future_games[1:]
        context['team'] = team
        return render(template_name='team/edit.html', request=request, context=context)

    if request.method == 'POST':
        if request.POST.get('team_name') != "":
            team.team_name = request.POST.get('team_name')
            team.save()

        return redirect(reverse('team:view', args=[team_id]))
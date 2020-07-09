from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from django.db.models import Q

from sluggers.models import Team, Match, Coach, Manager

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

        if len(past_games) > 0:
            context['past_games'] = past_games

        context['team'] = team
        return render(template_name='team/edit.html', request=request, context=context)

    if request.method == 'POST':
        if request.POST.get('team_name') != "":
            team.team_name = request.POST.get('team_name')
            team.save()

        c_first_name = request.POST.get('coach_first_name')
        c_last_name = request.POST.get('coach_last_name')
        c_phone_number = request.POST.get('coach_phone_number')
        c_email = request.POST.get('coach_email')

        m_first_name = request.POST.get('manager_first_name')
        m_last_name = request.POST.get('manager_last_name')
        m_phone_number = request.POST.get('manager_phone_number')
        m_email = request.POST.get('manager_email')

        coach_info = Coach.objects.get(coach_id=team.coach.coach_id)
        manager_info = Manager.objects.get(manager_id=team.manager.manager_id)

        
        coach_info.coach_first = c_first_name
        coach_info.coach_last = c_last_name
        coach_info.coach_phone = c_phone_number
        coach_info.coach_email = c_email
        coach_info.save()

        manager_info.coach_first = m_first_name
        manager_info.coach_last = m_last_name
        manager_info.coach_phone = m_phone_number
        manager_info.coach_email = m_email
        manager_info.save()

        return redirect(reverse('team:view', args=[team_id]))
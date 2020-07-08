from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from django.db.models import Max
from sluggers.models import Match, AgeGroup, Team

def view(request, match_id):
    context = {'match': Match.objects.get(match_id=match_id)}
    return render(template_name='match/view.html', request=request, context=context)

@login_required
def create(request):
    if request.method == "GET":
        context = {'agegroups': AgeGroup.objects.all(), 'teams': Team.objects.all()}
        return render(template_name="match/create.html", request=request, context=context)

    if request.method == 'POST':
        age_group = request.POST.get('age_group')
        home_team = request.POST.get('home_team')
        away_team = request.POST.get('away_team')
        game_date = request.POST.get('game_date')
        field = request.POST.get('field')

        ht = Team.objects.all().get(team_id=home_team)
        at = Team.objects.all().get(team_id=away_team)

        match_id = Match.objects.aggregate(Max('match_id'))['match_id__max'] + 1

        m = Match(match_id=match_id, home_team=ht, away_team=at, match_date=game_date)
        m.save()

        return redirect(reverse('team:edit', args=[home_team]))

@login_required
def edit(request, match_id):
    if request.method == "GET":
        return render(template_name="match/edit.html", request=request)

    if request.method == "POST":
        return redirect(reverse('match:view'))

@login_required
def delete(request, match_id):
    return redirect(reverse('team:edit'))
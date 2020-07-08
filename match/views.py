from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from django.db.models import Max
from sluggers.models import Match, AgeGroup, Team, Inning

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
        m = Match.objects.get(match_id=match_id)
        context = {'match': m, 'age_group': m.home_team.age_group.age_group_id, 'agegroups': AgeGroup.objects.all(), 'teams': Team.objects.all()}
        return render(template_name="match/edit.html", request=request, context=context)

    if request.method == "POST":
        age_group = request.POST.get('age_group')
        home_team = request.POST.get('home_team')
        away_team = request.POST.get('away_team')
        game_date = request.POST.get('game_date')
        field = request.POST.get('field')

        ht = Team.objects.all().get(team_id=home_team)
        at = Team.objects.all().get(team_id=away_team)

        m = Match.objects.all().get(match_id=match_id)

        m.home_team = ht
        m.away_team = at
        m.match_date = game_date

        # loop until we reach the end of entered innings in the html file
        for i in range(1, 20):
            # check if we were given this inning or not
            if 'i'+str(i)+'hr' not in request.POST:
                print('Breaking at: ' + str(i))
                # check if we have to delete any innings from the database
                for j in range(i, 20):
                    try:
                        inn = Inning.objects.all().get(match=m, inning_num=j)
                        inn.delete()
                    except Inning.DoesNotExist:
                        pass
                break
            else:
                # the inning was supplied, check to see if it previously existed
                try:
                    inn = Inning.objects.all().get(match=m, inning_num=i)
                    inn.home_hits = request.POST.get('i'+str(i)+'hh', 0)
                    inn.home_runs = request.POST.get('i'+str(i)+'hr', 0)
                    inn.home_errors = request.POST.get('i'+str(i)+'he', 0)
                    inn.away_hits = request.POST.get('i'+str(i)+'ah', 0)
                    inn.away_runs = request.POST.get('i'+str(i)+'ar', 0)
                    inn.away_errors = request.POST.get('i'+str(i)+'ae', 0)
                except Inning.DoesNotExist:
                    print('making: ' + str(i))
                    inn = Inning(match=m, inning_num=i, home_hits=request.POST.get('i'+str(i)+'hh', 0), home_runs=request.POST.get('i'+str(i)+'hr', 0), home_errors=request.POST.get('i'+str(i)+'he', 0), away_hits=request.POST.get('i'+str(i)+'ah', 0), away_runs=request.POST.get('i'+str(i)+'ar', 0), away_errors=request.POST.get('i'+str(i)+'ae', 0))
                inn.save()
                print(str(inn.inning_num) + " done")

        m.save()

        return redirect(reverse('match:view', args=[match_id]))

@login_required
def delete(request, match_id):
    return redirect(reverse('team:edit'))
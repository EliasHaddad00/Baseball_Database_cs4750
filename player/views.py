from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from django.db.models import Max
from sluggers.models import Player, AgeGroup, Team, EmergencyContact

def view(request, player_id):
    context = {'player': Player.objects.get(player_id=player_id)}
    return render(template_name='player/view.html', request=request, context=context)

@login_required
def edit(request, player_id):
    if request.method == "GET":
        return render(template_name='player/edit.html', request=request)

    if request.method == 'POST':
        return redirect(reverse('player:view'))

@login_required
def create(request):
    if request.method == "GET":
        context = {'agegroups': AgeGroup.objects.all(), 'teams': Team.objects.all()}
        return render(template_name='player/create.html', request=request, context=context)

    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        position = request.POST.get('position')
        uniform_number = request.POST.get('uniform_number')
        dob = request.POST.get('dob')
        age_group = request.POST.get('agegroup')
        team = request.POST.get('team')

        e_first_name = request.POST.get('emer_first_name')
        e_last_name = request.POST.get('emer_last_name')
        e_phone_number = request.POST.get('emer_phone_number')
        e_email = request.POST.get('emer_email')

        #grab all the ids we are going to use
        player_id = Player.objects.aggregate(Max('player_id'))['player_id__max'] + 1
        emer_id = EmergencyContact.objects.aggregate(Max('contact_id'))['contact_id__max'] + 1

        #create the emergency contact
        ec = EmergencyContact(contact_id=emer_id, contact_first=e_first_name, contact_last=e_last_name, contact_number=e_phone_number, contact_email=e_email)
        ec.save()

        #grab the team
        t = Team.objects.all().get(team_id=team)

        #finally, create the player
        p = Player(player_id=player_id, team=t, contact=ec, number=uniform_number, first_name=first_name, last_name=last_name, birth_date=dob, position=position)
        p.save()

        print(str(p.player_id) + "-" + p.first_name)

        return redirect(reverse('team:view', args=[team]))

@login_required
def delete(request, player_id):
    p = Player.objects.get(player_id=player_id)
    id = p.team.team_id
    p.delete()
    return redirect(reverse('team:edit', args=[id]) + "#players")

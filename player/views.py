from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from django.db.models import Max
from sluggers.models import Player, AgeGroup, Team, EmergencyContact, PitchingStats, BattingStats, FieldingStats

def view(request, player_id):
    context = {'player': Player.objects.get(player_id=player_id)}
    return render(template_name='player/view.html', request=request, context=context)

@login_required
def edit(request, player_id):
    if request.method == "GET":
        context = {'player': Player.objects.get(player_id=player_id), 'agegroups': AgeGroup.objects.all(), 'teams': Team.objects.all()}
        return render(template_name='player/edit.html', request=request, context=context)

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

        p = Player.objects.get(player_id=player_id)
        ec = EmergencyContact.objects.get(contact_id=p.contact.contact_id)
        t = Team.objects.get(team_id=team)

        ec.contact_first = e_first_name
        ec.contact_last = e_last_name
        ec.contact_number = e_phone_number
        ec.contact_email = e_email
        ec.save()

        p.first_name = first_name
        p.last_name = last_name
        p.position = position
        p.number = uniform_number
        p.birth_date = dob
        p.team = t

        p.save()

        try:
            for key, value in PitchingStats.get_fields_default(p.pitchingstats):
                setattr(p.pitchingstats, key, request.POST.get(key))
            p.pitchingstats.save()
        except:
            print('no pitch')
            pass

        try:
            for key, value in BattingStats.get_fields_default(p.battingstats):
                setattr(p.battingstats, key, request.POST.get(key))
            p.battingstats.save()        
        except:
            print('no bat')
            pass

        try:
            for key, value in FieldingStats.get_fields_default(p.fieldingstats):
               setattr(p.fieldingstats, key, request.POST.get(key))
            p.fieldingstats.save()   
        except:
            pass

        return redirect(reverse('player:view', args=[player_id]))

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

        PitchingStats(player_id, 0, 0, 0, 0, 0, 0, 0, 0).save()
        FieldingStats(player_id, 0, 0, 0, 0).save()
        BattingStats(player_id, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0).save()

        return redirect(reverse('team:view', args=[team]))

@login_required
def delete(request, player_id):
    p = Player.objects.get(player_id=player_id)
    id = p.team.team_id
    p.delete()
    return redirect(reverse('team:edit', args=[id]) + "#players")

from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required

from sluggers.models import Player

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
        return render(template_name='player/create.html', request=request)

    if request.method == 'POST':
        return redirect(reverse('team:edit'))

@login_required
def delete(request, player_id):
    return redirect(reverse('team:edit'))

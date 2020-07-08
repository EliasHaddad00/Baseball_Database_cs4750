from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required

from sluggers.models import Match

def view(request, match_id):
    context = {'match': Match.objects.get(match_id=match_id)}
    return render(template_name='match/view.html', request=request, context=context)

@login_required
def create(request):
    if request.method == "GET":
        return render(template_name="match/create.html", request=request)

@login_required
def edit(request, match_id):
    if request.method == "GET":
        return render(template_name="match/edit.html", request=request)

    if request.method == "POST":
        return redirect(reverse('match:view'))

@login_required
def delete(request, match_id):
    return redirect(reverse('team:edit'))
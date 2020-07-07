from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required


def view(request):
    return render(template_name='player/view.html', request=request)

@login_required
def edit(request):
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
def delete(request):
    return redirect(reverse('team:edit'))

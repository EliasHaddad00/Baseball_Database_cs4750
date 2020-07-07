from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required

def view(request):
    return render(template_name='team/view.html', request=request)

@login_required
def edit(request):
    if request.method == 'GET':
        return render(template_name='team/edit.html', request=request)

    if request.method == 'POST':
        return redirect(reverse('team:view'))
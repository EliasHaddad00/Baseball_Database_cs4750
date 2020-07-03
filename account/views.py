from django.shortcuts import render, redirect, reverse
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login


@login_required
def view(request):
    return render(template_name='account/view.html', request=request)

def create(request):
    if request.method == "POST":
        u = User.objects.create_user(request.POST.get('email'), request.POST.get('email'), password=request.POST.get('password'))
        u.first_name = request.POST.get('first_name')
        u.last_name = request.POST.get('last_name')
        u.save()
        login(request, u)
        return redirect(reverse('profile:view'))
    elif request.method == 'GET':
        return render(template_name='account/create.html', request=request)
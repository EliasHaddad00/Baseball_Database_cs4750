from django.shortcuts import render, redirect, reverse
from django.http import JsonResponse, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login as auth_login, authenticate, logout as auth_logout
from django.db.utils import IntegrityError



def red(request):
    if request.user.is_authenticated:
        return redirect(reverse('profile:view', args=[request.user.id]))
    else:
        return redirect(reverse('profile:login'))

@login_required
def view(request, profile_id):
    return render(template_name='account/view.html', request=request)

def create(request):
    if request.method == "POST":
        u = User.objects.create_user(request.POST.get('email'), request.POST.get('email'), password=request.POST.get('password'))
        u.first_name = request.POST.get('first_name')
        u.last_name = request.POST.get('last_name')
        u.save()
        auth_login(request, u)
        return redirect(reverse('profile:redirect'))
    elif request.method == 'GET':
        return render(template_name='account/create.html', request=request)

def edit(request):
    if request.method == "POST":
        #u = User.objects.create_user(request.POST.get('email'), request.POST.get('email'), password=request.POST.get('password'))
        u = request.user
        u.first_name = request.POST.get('first_name')
        u.last_name = request.POST.get('last_name')

        if request.POST.get('email') != "" and request.POST.get('email') != request.user.email:
            u.email = request.POST.get('email')
            u.username = request.POST.get('email')

        if request.POST.get('password') != "":
            u.set_password(request.POST.get('password'))

        try:
            u.save()
        except IntegrityError:
            return HttpResponse("This email address is already in use, please use a different one")
        return redirect(reverse('profile:redirect'))
    elif request.method == 'GET':
        return render(template_name='account/edit.html', request=request)

def login(request):
    if request.method == "POST":
        u = authenticate(username=request.POST.get('email'), password=request.POST.get('password'))
        print(u)
        if u is None:
            return render(template_name='account/login.html', request=request)
        auth_login(request, u)
        return redirect(reverse('profile:redirect'))
    elif request.method == 'GET':
        if request.user.is_authenticated:
            return redirect(reverse('sluggers:landing'))
        return render(template_name='account/login.html', request=request)

def logout(request):
    if request.user.is_authenticated:
        auth_logout(request)
    return redirect(reverse('sluggers:landing'))
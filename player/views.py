from django.shortcuts import render, redirect, reverse

def view(request):
    return render(template_name='player/view.html', request=request)

def edit(request):
    if request.method == "GET":
        return render(template_name='player/edit.html', request=request)

    if request.method == 'POST':
        return redirect(reverse('team:view'))
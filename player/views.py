from django.shortcuts import render

def view(request):
    return render(template_name='player/view.html', request=request)
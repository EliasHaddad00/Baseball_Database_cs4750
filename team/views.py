from django.shortcuts import render

# Create your views here.

def view(request):
    return render(template_name='team/view.html', request=request)
from django.shortcuts import render

def view(request):
    return render(template_name='account/view.html', request=request)
from django.shortcuts import render

def view(request):
    return render(template_name='match/view.html', request=request)
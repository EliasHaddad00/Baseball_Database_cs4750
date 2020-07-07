from django.shortcuts import render
from django.contrib.auth.decorators import login_required

def view(request):
    return render(template_name='match/view.html', request=request)

@login_required
def create(request):
    if request.method == "GET":
        return render(template_name="match/create.html", request=request)
from django.shortcuts import render
from django.http import HttpResponse
from .models import AgeGroup

def index(request):
    context={'agegroups': AgeGroup.objects.all()}
    return render(template_name='sluggers/landing.html', request=request, context=context)
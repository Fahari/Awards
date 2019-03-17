from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from . models import *

# Create your views here.
def home(request):
    return render(request, 'home.html')

@login_required(login_url='/accounts/login/')
def profile(request):
    current_user = request.user
    profile = Profile.objects.all()
    pics = Image.objects.all()

    return render(request, 'registration/profile.html',locals())

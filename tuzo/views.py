from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from . models import *
from .forms import *

# Create your views here.
def home(request):
    return render(request, 'home.html')

@login_required(login_url='/accounts/login/')
def profile(request):
    current_user = request.user
    profile = Profile.objects.all()
    pics = Image.objects.all()

    u_form = UserUpdateForm()
    p_form = ProfileUpdateForm()

    context = {
        'u_form':u_form,
        'p_form':p_form
    }

    return render(request, 'registration/profile.html',locals())

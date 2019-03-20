from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from . models import *
from .forms import *

# Create your views here.
def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'home.html',context)

@login_required(login_url='/accounts/login/')
def profile(request):
    current_user = request.user
    profile = Profile.objects.all()
    pics = Image.objects.all()

    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST,instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES,instance=request.user.profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            # message.success(request, f'Your account has been updated')
            return render(request,'registration/profile.html')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)


    context = {
        'u_form':u_form,
        'p_form':p_form
    }

    return render(request, 'registration/profile.html',locals())

class PostListView(ListView):
    model = Post
    template_name = 'home.html'
    context_object_name = 'posts'

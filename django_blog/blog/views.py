from django.shortcuts import render,redirect
from .models import Post
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .forms import UserForm, ProfileForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login

# Create your views here.

def homeView(request):
    return render(request, 'blog/base.html')
def PostView(request):
    posts = Post.objects.all()
    return render(request, 'blog/post.html', {'posts': posts})

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()  # Save the new user
            login(request, user)  # Log them in immediately
            return redirect('home')  # Use a URL name, not a template file
    else:
        form = UserCreationForm()

    return render(request, 'blog/register.html', {'form': form})

        
def Login_View(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect (request.POST)
        else:
                return redirect("home") 
    else:
        form = AuthenticationForm()
        return render(request, 'blog/login.html', {'form':form})

@login_required
def profile_view(request):
    if request.method == "POST":
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('profile')  # Redirect back to profile page after saving
    else:
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)

    return render(request, 'blog/profile.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })
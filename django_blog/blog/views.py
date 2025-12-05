from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth import login, update_session_auth_hash
from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm

# Create your views here.

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('profile')
    else:
        form = CustomUserCreationForm()
    return render(request, 'blog/register.html', {'form': form})


def profile(request):
    if request.method == 'POST':
        form = UserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.instance)  # Keeps the user logged in after updating password
            return redirect('profile')
    else:
        form = UserChangeForm(instance=request.user)
    return render(request, 'blog/profile.html', {'form': form})

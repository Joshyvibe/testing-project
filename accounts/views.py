# accounts/views.py

from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.models import User
from django.core.management import call_command
from django.http import JsonResponse


def create_superuser_view(request):
    # Check if the request is authorized
    # Implement your authentication logic here

    # Call the createsuperuser management command
    call_command('createsuperuser', username='admin', email='admin@example.com', password='admin', interactive=False)

    # Check if the superuser has been successfully created
    try:
        user = User.objects.get(username='admin')
        return JsonResponse({'message': 'Superuser created successfully', 'user': {'username': user.username, 'email': user.email}})
    except User.DoesNotExist:
        return JsonResponse({'message': 'Failed to create superuser'}, status=500)


def home(request):
    return render(request, 'accounts/home.html')

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'accounts/signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('home')

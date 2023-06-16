from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.urls import reverse, resolve

from myapp.models import MyUsers


def index_view(request):
    return render(request, 'index.html')


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('landing')  # Redirect to the home page

        else:
            # Invalid credentials, show an error message
            error_message = "Invalid username or password."
            return render(request, 'login.html', {'error_message': error_message})
    else:
        return render(request, 'login.html')


def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            MyUsers.objects.create(
                user=form.save(),
                user_data=0
            )
            # MyUsers.save()
            return redirect('login')  # Redirect to the login page after successful signup
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})


def landing_view(request):
    user = request.user
    my_user = MyUsers.objects.get(user=user)

    if request.method == 'POST':
        if 'increment' in request.POST:
            my_user.user_data += 1
            my_user.save()
        elif 'decrement' in request.POST:
            my_user.user_data -= 1
            my_user.save()
        return redirect('landing')

    context = {
        'username': my_user.user.username,
        'user_data': my_user.user_data
    }
    return render(request, 'landing.html', context)

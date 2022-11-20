from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import connection
from .forms import connectionForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
# from django.contrib.auth.forms import UserCreationForm
from django.views.decorators.csrf import csrf_exempt
# from django.urls import reverse, reverse_lazy


def home(request):
    return render(request, 'index.html', {})


@csrf_exempt
def login_user(request):
    if request.user.is_authenticated:
        return redirect('chat')
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            request.session['name'] = username
            request.session['profile_photo'] = "https://s3-us-west-2.amazonaws.com/s.cdpn.io/1940306/chat_avatar_03.jpg"
            request.session['is_login'] = True
            messages.success(request, "Login Sucessful")
            # return redirect ('chat')
            all_connections = connection.objects.all
            return render(request, 'chat.html', {'connections': all_connections})
        else:
            messages.error(request, "Invalid Credentials")
            return render(request, 'login.html', {})
    else:
        return render(request, 'login.html', {})


@csrf_exempt
def logout_user(request):
    logout(request)
    messages.success(request, "Logout Sucessful")
    return redirect('login')


@csrf_exempt
def profile(request):
    if request.method == "POST":
        name = request.POST["name"]
        photo = request.POST["photo"]
        return render(request, 'profile.html', {'name': name, 'photo': photo})


@csrf_exempt
def signup(request):
    if request.user.is_authenticated:
        return redirect('chat')
    else:
        if request.method == "POST":
            if request.POST['password1'] == request.POST['password2']:
                user = User.objects.create_user(
                    request.POST['name'], '', request.POST['password1'])
                user.save()
                messages.success(
                    request, "Signup Sucessful! Please Login to continue.")
                return render(request, 'login.html', {})
            else:
                messages.error(
                    request, "Signup Unsucessful! Please try again.")
                return render(request, 'signup.html', {})

        else:
            return render(request, 'signup.html', {})


@csrf_exempt
def chat(request):
    if request.user.is_authenticated:
        all_connections = connection.objects.all
        return render(request, 'chat.html', {'connections': all_connections})
    else:
        return redirect('login')


@csrf_exempt
def video(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            all_connections = connection.objects.all
            name = request.POST["name"]
            photo = request.POST["photo"]
            return render(request, 'video.html', {'connections': all_connections, 'name': name, 'photo': photo})
    else:
        return redirect('login')


def chat_clicked(request):
    return render(request, 'done')
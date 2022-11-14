from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import connection
from .forms import connectionForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
# from django.contrib.auth.forms import UserCreationForm
# from django.views.decorators.csrf import csrf_exempt

def home(request):
    return render(request, 'index.html', {})

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
            redirect ('chat')
            # all_connections = connection.objects.all
            # return render(request, 'chat.html', { 'connections': all_connections })
        else:
            return render(request, 'login.html', {})
    else:
        return render(request, 'login.html', {})

# @csrf_exempt
def signup(request):
    if request.user.is_authenticated:
        return redirect('chat')
    if request.method == "POST":
        if request.POST['password1'] == request.POST['password2']:
            user = User.objects.create_user(request.POST['name'], '', request.POST['password1'])
            user.save()
            return redirect('login')
        else:
            messages.error(request, "Signup Unsucessful)
            return render(request, 'signup.html', {})
    else:
        return render(request, 'signup.html', {})

def chat(request):
    if ~request.user.is_authenticated:
        return redirect('login')
    all_connections = connection.objects.all
    return render(request, 'chat.html', { 'connections': all_connections })

def video(request):
    if ~request.user.is_authenticated:
        return redirect('login')
    all_connections = connection.objects.all
    return render(request, 'video.html', { 'connections': all_connections })

def chat_clicked(request):
    return render(request, 'done')
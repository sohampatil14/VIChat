from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import connection
from .forms import connectionForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
# from django.views.decorators.csrf import csrf_exempt

def home(request):
    return render(request, 'index.html', {})

def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            request.session['name'] = username
            request.session['profile_photo'] = "https://s3-us-west-2.amazonaws.com/s.cdpn.io/1940306/chat_avatar_03.jpg"
            messages.success(request, "Login Sucessful")
            return redirect('chat')
        else:
            return render(request, 'login.html', {})
    else:
        return render(request, 'login.html', {})

# @csrf_exempt
def signup(request):
    if request.method == "POST":
        form = connectionForm(request.POST or None)
        if form.is_valid():
            form.save()
        else:
            name = request.POST['name']
            password = request.POST['password']
            profile_photo = request.POST['profile_photo']
            messages.error(request, "Sign Up Unsucessful")
            return render(request, 'signup.html', {
                'name':name, 
                'password':password, 
                'profile_photo':profile_photo,
                })
        messages.success(request, "Sign Up Sucessful")
        return redirect('login')

    else:
        return render(request, 'signup.html', {})

def chat(request):
    all_connections = connection.objects.all
    return render(request, 'chat.html', { 'connections': all_connections })

def video(request):
    all_connections = connection.objects.all
    return render(request, 'video.html', { 'connections': all_connections })

def chat_clicked(request):
    return render(request, 'done')
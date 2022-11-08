from django.shortcuts import render
from django.http import HttpResponse
from .models import connection

def home(request):
    return render(request, 'index.html', {})

def login(request):
    return render(request, 'login.html', {})

def signup(request):
    return render(request, 'signup.html', {})

def chat(request):
    all_connections = connection.objects.all
    return render(request, 'chat.html', { 'connections': all_connections })

def video(request):
    all_connections = connection.objects.all
    return render(request, 'video.html', { 'connections': all_connections })

def chat_clicked(request):
    return render(request, 'done')

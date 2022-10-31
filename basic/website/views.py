from django.shortcuts import render
from django.http import HttpResponse

context = {
    'connections' : ['Vincet Porter', 'Prénom Nom'],
    'profile_photo' : ['static\website\images\chat_avatar_01.png', 'template_and_routing\basic\website\static\website\images\chat_avatar_02.png'],
    'is_started' : [False, False]
}

context['people'] = zip(context['connections'], context['profile_photo'])

def home(request):
    return render(request, 'index.html', {})

def login(request):
    return render(request, 'login.html', {})

def chat(request):
    return render(request, 'chat.html', context)

def chat_clicked(request):
    return render(request, 'done')

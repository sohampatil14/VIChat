from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import connection
from .models import Account
from .forms import connectionForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
# from django.contrib.auth.forms import UserCreationForm
from django.views.decorators.csrf import csrf_exempt
# from django.urls import reverse, reverse_lazy
import secrets


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
                account = Account(
                    user=user, status='Not Available', userID=secrets.token_hex(3))
                account.userID = secrets.token_hex(3)
                account.save()
                messages.success(
                    request, "Signup Sucessful! Please Login to continue.")
                return render(request, 'login.html', {})
                # return render(request, 'profile_create.html', {})
                # user = authenticate(request, username=request.POST['name'], password=request.POST['password1'])
                # if user is not None:
                #     login(request, user)
                #     request.session['name'] = request.POST['name']
                #     request.session['profile_photo'] = "https://s3-us-west-2.amazonaws.com/s.cdpn.io/1940306/chat_avatar_03.jpg"
                #     request.session['is_login'] = True
                #     messages.success(request, "Login Sucessful")
                #     return redirect('chat')
                # else:
                #     return redirect('login')
            # form = UserCreationForm(request.POST)# or None)
            # if form.is_valid():
            #     form.save()
            #     username = form.cleaned_data['name']
            #     password = form.cleaned_data['password1']
            #     # password2 = form.cleaned_data['password2']
            #     user = authenticate(username=username, password=password)
            #     login(request, user)
            #     return redirect('chat')
            else:
                messages.error(
                    request, "Signup Unsucessful! Please try again.")
                return render(request, 'signup.html', {})
            #     name = request.POST['name']
            #     password1 = request.POST['password1']
            #     password2 = request.POST['password2']
            #     messages.error(request, "Sign Up Unsucessful")
            #     return render(request, 'signup.html', {
            #         'name':name,
            #         'password':password,
            #         'profile_photo':profile_photo,
            #         })
            # messages.success(request, "Sign Up Sucessful")
            # return redirect('login')

        else:
            return render(request, 'signup.html', {})


@csrf_exempt
def profile_create(request):
    if request.method == "POST":
        request.session['status'] = request.POST['status']
        messages.success(request, "Profile Creation Successful.")
        return render(request, 'login.html', {})
    return render(request, 'profile_create.html', {})


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


# https://www.youtube.com/playlist?list=PLCC34OHNcOtqW9BJmgQPPzUpJ8hl49AGy
# https://stackoverflow.com/questions/1061279/for-the-django-admin-how-do-i-add-a-field-to-the-user-model-and-have-it-editabl
# https://www.youtube.com/watch?v=EqjRhO5CK6A&list=PLCC34OHNcOtqW9BJmgQPPzUpJ8hl49AGy&index=25
# https://www.youtube.com/watch?v=sSKYEMEU-C8 -- code editor
# https://www.youtube.com/playlist?list=PLOLrQ9Pn6cayYycbeBdxHUFrzTqrNE7Pe -- db course
# https://www.youtube.com/watch?v=kRJpQxi2jIo -- modified user fileds

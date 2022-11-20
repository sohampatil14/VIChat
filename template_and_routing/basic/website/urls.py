from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('login/', views.login_user, name="login"),
    path('signup/', views.signup, name="signup"),
    path('chat/', views.chat, name="chat"),
    path('video/', views.video, name="video"),
    path('logout/', views.logout_user, name="logout"),
    path('profile/', views.profile, name="profile"),
    # path('chat/0/', views.chat_clicked, name = "chat_clicked"),
]

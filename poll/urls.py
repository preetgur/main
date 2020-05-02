from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [

    path("home",views.home,name="home"),
    path("",views.index,name="poll"),
    path("total_polls",views.total_polls,name="total_polls"),
    path('give_vote/<str:pk>',views.give_vote,name="give_vote"),
    path('result/<str:poll_id>',views.result,name="result"),
    path('ajax_json/<str:poll_id>',views.ajax_json_response,name="ajax_json"),



    path('signup',views.signup,name="signup"),
    path('login',auth_views.LoginView.as_view(template_name="poll/login.html"),name="login"),
    path('logout',auth_views.LogoutView.as_view(template_name="poll/poll_index.html"),name="logout"),



]
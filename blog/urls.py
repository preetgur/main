from blog import views
from django.urls import path

urlpatterns = [
    path("",views.index,name="blog_index"),
    path("dashboard",views.dashboard,name="dashboard"),
    path("all_blogs",views.create_blog,name="all_blogs"),
    path("show_blogs",views.show_blogs,name="show_blogs"),
    path("detail/<str:pk>",views.detail_blog,name="detail_blog"),
    path("like/<str:comment_id>/<str:option>/<str:blog_id>",views.like,name="like"),

    path("profile",views.profile,name="profile"),
    path("question",views.question,name="question"),

    ## api
    path("profile_api",views.profile_api,name="profile_api"),
    path("all_profile_api",views.all_profile_api,name="all_profile_api"),

]
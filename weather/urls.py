from django.urls import path
from weather import views

urlpatterns = [

    path("",views.index,name="weather_index")
]
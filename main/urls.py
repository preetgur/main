"""main URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('weather',include("weather.urls")),
    path('student',include("student.urls")),
    path("poll/",include('poll.urls')),
<<<<<<< HEAD
    path("",include('blog.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),

    path("forms/",include('d_forms.urls')),


]

# media files
from django.conf.urls.static import static
from django.conf import settings


urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
=======


]
>>>>>>> 55fe3e4c34ff151a9c3852917123362152c84fc7

from django.urls import path,re_path
from django.views.generic import TemplateView
from . import views

from blog.models import Blog
all_blogs = Blog.objects.all()
total_blog = all_blogs.count()

urlpatterns = [

    path("",TemplateView.as_view(template_name = "d_forms/index.html",extra_context = {'data':all_blogs}),{'on_sale':all_blogs}), # rendering a template without view quickest way to do

    path("about",views.AboutIndex.as_view(extra_context={"total":total_blog}),{'data':all_blogs,'tot':total_blog}),

    path("filter",views.filterIndex.as_view()),
    path("form",views.formIndex),

]
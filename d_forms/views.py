from django.views.generic import TemplateView
from blog.models import Blog
class AboutIndex(TemplateView):
      template_name = 'd_forms/about.html'

      def get_context_data(self, **kwargs):
         # **kwargs contains keyword context initialization values (if any)
        #  print(" @@@ data @@@",kwargs['tot'])
        #  print(" @@@ data @@@",kwargs['total']) gives error

         # Call base implementation to get a context sepecigy in urls
         context = super(AboutIndex ,self).get_context_data(**kwargs)

         print(context['total'],"###")
         print(context['view'])
         
         # Add context data to pass to template
         context['aboutdata'] = 'Custom data'
         return context


class filterIndex(TemplateView):

      template_name = "d_forms/filter.html"

      def get_context_data(self, **kwargs):

            context = super().get_context_data(*kwargs)

            blogs = Blog.objects.all()

            context['blog'] = blogs
            context['stores'] = [
                  {'name': 'Downtown', 'street': '385 Main Street', 'city': 'San Diego'},
                  {'name': 'Uptown', 'street': '231 Highland Avenue', 'city': 'San Diego'},
                  {'name': 'Midtown', 'street': '85 Balboa Street', 'city': 'San Diego'},
                  {'name': 'Downtown', 'street': '639 Spring Street', 'city': 'Los Angeles'},
                  {'name': 'Midtown', 'street': '1407 Broadway Street', 'city': 'Los Angeles'},
                  {'name': 'Downton', 'street': '50 1st Street', 'city': 'San Francisco'},
                  ]
            return context

from .forms import Contact_Form
from django.shortcuts import render
from django.http import HttpResponseRedirect,HttpResponse


def formIndex(request):
      if request.method == "GET":
            form = Contact_Form()

      if request.method == "POST":
            form = Contact_Form(request.POST)

            if form.is_valid():
                  name = form.cleaned_data['name']
                  # return HttpResponse(f"<b>{name}</b>, your data is saved. Thanks for your time!")  
                  return HttpResponseRedirect('/forms/form')
            

      context = { 
                  "form":form,
      }
      return render(request,"d_forms/forms.html",context)      

            
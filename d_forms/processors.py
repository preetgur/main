# create custom "context processor"

from blog.models import Blog


def context_blog(request):
    blog  = Blog.objects.all()
    context = {'context_data': blog}
    return {'context_data': blog}

# add this custom processor to "settings.py" in "context_processors" in "OPTIONS"

""" 
'context_processors': [
                # appname.filename.methodname
                'd_forms.processors.context_blog', 
                    ]
"""
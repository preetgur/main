from django.contrib import admin
from blog.models import Blog,Images,Profile,ProfileInterest,Comment,Like,DisLike,User_Additional_Info,Blog_category
# Register your models here.

# Inorder to use tinymce
# @admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):

    class Media:
        js = ("blog/js/tinyinject.js",) 
        # not single qoute ' '

# admin.site.register(Blog,BlogAdmin)
admin.site.register(Blog)
admin.site.register(Blog_category)
admin.site.register(Images)
admin.site.register(Comment)
admin.site.register(Like)
admin.site.register(DisLike)
admin.site.register(User_Additional_Info)



# for add btn
admin.site.register(ProfileInterest)
admin.site.register(Profile)



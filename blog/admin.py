from django.contrib import admin
from blog.models import Blog,Images,Profile,ProfileInterest,Comment,Like,DisLike,User_Additional_Info
# Register your models here.

admin.site.register(Blog)
admin.site.register(Images)
admin.site.register(Comment)
admin.site.register(Like)
admin.site.register(DisLike)
admin.site.register(User_Additional_Info)



# for add btn
admin.site.register(ProfileInterest)
admin.site.register(Profile)


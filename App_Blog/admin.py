from django.contrib import admin
from . models import Blog, Comment, Likes
# Register your models here.
# TO DISPLAY ALL TABLES OR MODELS IN SUPERUSERS ADMIN WE NEED TO REGISTER models
admin.site.register(Blog)
admin.site.register(Comment)
admin.site.register(Likes)

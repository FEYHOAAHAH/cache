from django.contrib import admin

from blogapp.models import Tag, Post

admin.site.register(Tag)
admin.site.register(Post)

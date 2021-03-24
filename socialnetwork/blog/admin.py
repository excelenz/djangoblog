from django.contrib import admin
from .models import Post
from socialnetwork.models import Account


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'created_on')
    list_filter = ("status",)
    search_fields = ['title', 'content']


admin.site.register(Post, PostAdmin)
#admin.site.register(Account)
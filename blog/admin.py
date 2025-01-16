from django.contrib import admin
from .models import Post
# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ('title','date')
    search_fields=('title',)
    list_filter=('date',)
admin.site.register(Post,PostAdmin)
from django.contrib import admin
from apps.blog.models import BlogModel

# Register your models here.
class BlogModelAdmin(admin.ModelAdmin):
    pass

admin.site.register(BlogModel, BlogModelAdmin)
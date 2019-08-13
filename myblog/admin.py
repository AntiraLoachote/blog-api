from django.contrib import admin

from .models import Post

# Register your models here.


# admin.site.register(Post)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_per_page = 30
    list_display = (
        'id',
        'text',
        'created_date',
        'author'
    )
    search_fields = (
        'text',
        'author',
    )

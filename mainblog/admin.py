from django.contrib import admin
from .models import Post, Comment, Category

class CommentInline(admin.StackedInline):
    model = Comment

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'descr', 'pub_date', 'category')
    inlines = [CommentInline]

admin.site.register(Post, PostAdmin)



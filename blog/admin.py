from django.contrib import admin
from .models import Post, Comment
from django_summernote.admin import SummernoteModelAdmin
from .models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status', 'pub_date')
    list_filter = ("status",)
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'content', 'post', 'pub_date', 'active')
    list_filter = ('active', 'pub_date')
    search_fields = ('name', 'email', 'content')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(active=True)


class PostAdmin(SummernoteModelAdmin):
    summernote_fields = ('content',)


admin.site.register(Post, PostAdmin)

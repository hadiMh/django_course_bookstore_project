from django.contrib import admin

from .models import Book, Comment

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'book', 'text', 'datetime_created', )


admin.site.register(Book)
# admin.site.register(Comment, CommentAdmin)

from django.contrib import admin

from .models import Comment


# Register your models here.
class CommentAdmin(admin.ModelAdmin):
	list_display = (
		'comment_author',
		'comment_date',
		'comment_text'
		)
	list_filter = ['comment_date', 'comment_author']
	search_fields = ['comment_author']
	readonly_fields = ('comment_date',)
	fieldsets = [
		(None, {'fields': ['comment_author', 'comment_text']})
		]

admin.site.register(Comment, CommentAdmin)
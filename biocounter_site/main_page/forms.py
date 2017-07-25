from django.forms import ModelForm
from django.utils import timezone


from .models import Comment


class CommentsForm(ModelForm):
	class Meta:
		model = Comment
		fields = ['comment_author', 'comment_text']
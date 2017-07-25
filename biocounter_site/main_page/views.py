from django.contrib import messages
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.views.generic import TemplateView
from django.utils import timezone

from .models import Comment
from .forms import CommentsForm


# Create your views here.
class IndexView(TemplateView):
	template_name = 'main_page/index.html'


class DownloadView(TemplateView):
	template_name = 'main_page/download.html'


class FeaturesView(TemplateView):
	template_name = 'main_page/features.html'


class SupportView(TemplateView):
	template_name = 'main_page/support.html'


class CommentsView(TemplateView):
	template_name = 'main_page/comments.html'

	def get(self, request, *args, **kwargs):
		last_comments_list = Comment.objects.filter(comment_date__lte=timezone.now()).order_by('-comment_date')[:40]
		form = CommentsForm()
		context = {
			'last_comments_list': last_comments_list,
			'form': form
			}		

		return render(request, self.template_name, context)

	def post(self, request, *args, **kwargs):
		form = CommentsForm(request.POST)
		if form.is_valid():
			messages.success(request, 'Thank You for Your comment.')
			form.save()
			form = CommentsForm()			

			return HttpResponseRedirect(reverse('comments'))

		else:
			form = CommentsForm()
			context['form'] = form

			return render(request, template_name, context)

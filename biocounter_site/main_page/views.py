from django.contrib import messages
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.template import loader
from django.urls import reverse
from django.views import generic
from django.utils import timezone

from .models import Comment
from .forms import CommentsForm


# Create your views here.
def index(request):
	template_name = 'main_page/index.html'

	return render(request, template_name)

def download(request):
	template_name = 'main_page/download.html'

	return render(request, template_name)

def features(request):
	template_name = 'main_page/features.html'

	return	render(request, template_name)

def support(request):
	template_name = 'main_page/support.html'

	return	render(request, template_name)

def comments(request):
	template_name = 'main_page/comments.html'
	last_comments_list = Comment.objects.filter(comment_date__lte=timezone.now()).order_by('-comment_date')[:40]
	context = {
		'last_comments_list': last_comments_list
		}

	if request.method == 'POST':
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

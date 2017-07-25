import datetime

from django.db import models
from django.utils import timezone


# Create your models here.
class Comment(models.Model):
	comment_author = models.CharField(max_length=50)
	comment_date = models.DateTimeField(auto_now_add=True)
	comment_text = models.TextField(max_length=1000)
	
	def __str__(self):
		return 'Author: {}, Date: {}, Comment: {}.'.format(
			self.comment_author,
			self.comment_date,
			self.comment_text
			)

	def was_published_recently(self):
		now = timezone.now()

		return now - datetime.timedelta(days=7) < self.comment_date <= now

	was_published_recently.admin_order_field = 'comment_date'
	was_published_recently.boolean = True
	was_published_recently.short_description = 'Published recently'
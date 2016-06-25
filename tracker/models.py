from django.db import models
from django.utils import timezone

dateFormatStr = '%H%Mz %a %b %d'

class Chart(models.Model):
	validDate = models.DateTimeField(default=timezone.now)
	title = models.CharField(max_length=120)
	description = models.TextField()
	image = models.ImageField(upload_to='charts')
	isArchived = models.BooleanField(default=False)

class Discussion(models.Model):
	author = models.ForeignKey('auth.User')
	validDate = models.DateTimeField(default=timezone.now)
	text = models.TextField()

	def __str__(self):
		return self.author.username + ' at ' + self.validDate.strftime(dateFormatStr)

class Event(models.Model):
	title = models.CharField(max_length=120)
	createdDate = models.DateTimeField(default=timezone.now)
	owner = models.ForeignKey('auth.User')
	discussions = models.ManyToManyField(Discussion,verbose_name='discussion timeline',blank=True)
	isPublic = models.BooleanField(default=False,verbose_name='share this event with other users')

	def __str__(self):
		allDiscussionDates = [x.validDate for x in self.discussions.all()]
		allDiscussionDates.sort()
		if len(allDiscussionDates) >= 2:
			return '{0:s} ({1:s} to {2:s})'.format(self.title, allDiscussionDates[0].strftime(dateFormatStr), allDiscussionDates[-1].strftime(dateFormatStr))
		elif len(allDiscussionDates) == 1:
			return '{0:s} ({1:s})'.format(self.title, allDiscussionDates[0].strftime(dateFormatStr))
		else:
			return '{0:s} (no discussions)'.format(self.title)
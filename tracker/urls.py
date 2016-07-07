"""
    Copyright 2016 Jake Wimberley.

    This file is part of RunToRun.

    RunToRun is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    RunToRun is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with RunToRun.  If not, see <http://www.gnu.org/licenses/>.
"""
from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.home, name='home'),
  url(r'^discussions/(\d{8}_\d{4})/(\d{8}_\d{4})/$', views.discussionRange),
  url(r'^discussions/$', views.allDiscussions),
  url(r'^addConcurrent/(\d+)/$', views.concurrentDiscussion, name='addConcurrent'),
  url(r'^newEvent/$', views.newEvent, name='newEvent'),
  url(r'^event/(\d+)/$', views.singleEvent, name='singleEvent'),
]

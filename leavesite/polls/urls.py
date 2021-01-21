"""
Not part of django package, just added based on the tutorial
"""

from django.conf.urls import url
from . import views
app_name = 'polls'
urlpatterns = [
    # 127.0.0.1/polls
    # ^$ do not add anything to the , # 2 calls the views > index function
    url(r'^$', views.index, name="index"),

    #127.0.0.1/polls/1
    url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),

    #127.0.0.1/polls/1/results
    url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name="results"),

    #127.0.0.1/polls/1/vote
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name="vote"),
]

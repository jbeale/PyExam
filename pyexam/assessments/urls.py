from django.conf.urls import patterns, url

import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^startexam/(?P<activityCode>\d+)/$', views.redeemActivityCode, name="redeemActivityCode"),
    url(r'^take/(?P<takeId>\d+)/$', views.getQuestionPage, name="getQuestionPage"),
    url(r'^take/(?P<takeId>\d+)/answercheck$', views.guess, name="guess")
)
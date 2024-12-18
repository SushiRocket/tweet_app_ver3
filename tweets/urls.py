from django.urls import path
from . import views

app_name = 'tweets'

urlpatterns = [
    path('', views.tweet_list, name='tweet_list'),
]
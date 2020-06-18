from django.urls import path
from tweet import views

urlpatterns = [
    path('', views.main, name="homepage"),
    path('tweet/', views.post_tweet),
    path('profile/<str:username>/', views.profile, name='profile'),
    # path('twitteruser/<int:userid>/', views.profile),
    path('tweetdetail/<int:id>/', views.tweet_detail),
    path('userdetail/<int:id>/', views.user_detail),
]

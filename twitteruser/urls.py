from django.urls import path
from twitteruser import views

urlpatterns = [
    path('following/<int:id>/', views.follow),
    path('unfollowing/<int:id>/', views.unfollow),
]

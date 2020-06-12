from django.urls import path
from tweet import views

urlpatterns = [
    path('', views.main, name="homepage"),
    path('tweet/', views.post_tweet),
    # path('profile/', views.profile),
]

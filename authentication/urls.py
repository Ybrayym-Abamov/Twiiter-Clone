from django.urls import path
from authentication import views

urlpatterns = [
    path('login/', views.login_view, name='loginpage'),
    path('logout/', views.logout_view),
    path('signup/', views.signup_view)
]

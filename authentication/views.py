from django.shortcuts import render, reverse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from twitteruser.models import TwitterUser
from authentication.forms import LoginForm, SignUpForm


# Create your views here.
def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(request, username=data['username'], password=data['password'])
            if user:
                login(request, user)
                return HttpResponseRedirect(request.GET.get('next', reverse('homepage')))
    form = LoginForm()
    return render(request, 'login.html', {"form": form})


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('loginpage'))


def signup_view(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = TwitterUser.objects.create_user(
                username=data['username'],
                password=data['password'],
                displayname=data['displayname']
            )
            if user:
                login(request, user)
                return HttpResponseRedirect(reverse('loginpage'))
    form = SignUpForm()
    return render(request, 'signup.html', {"form": form})

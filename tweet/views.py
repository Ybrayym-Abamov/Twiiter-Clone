from django.shortcuts import render, reverse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from tweet.models import Tweet
from tweet.forms import TweetForm
from twitteruser.models import TwitterUser


# Create your views here.


def post_tweet(request):
    if request.method == "POST":
        form = TweetForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            twitteruser = TwitterUser.objects.get(id=request.user.id)
            message_box = Tweet.objects.create(
                message_box=data['message_box'],
                twitteruser=twitteruser
            )
        return HttpResponseRedirect(reverse('homepage'))
    form = TweetForm()
    return render(request, 'tweet.html', {'form': form})


def main(request):
    data = Tweet.objects.all()
    return render(request, 'main.html', {'data': data})

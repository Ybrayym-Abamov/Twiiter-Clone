from django.shortcuts import render, reverse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from tweet.models import Tweet
from tweet.forms import TweetForm
from twitteruser.models import TwitterUser
from notification.models import Notification
import re


@login_required
def post_tweet(request):
    if request.method == "POST":
        form = TweetForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            twitteruser = request.user
            messagebox = Tweet.objects.create(
                messagebox=data['messagebox'],
                this_user=twitteruser
            )
            # notification
            if '@' in messagebox.messagebox:
                username = re.findall(r'@(\w+)', messagebox.messagebox)
                for user in username:
                    target = TwitterUser.objects.get(username=user)
                    Notification.objects.create(
                        messagebox=messagebox,
                        target_user=target
                    )
        return HttpResponseRedirect(reverse('homepage'))
    form = TweetForm()
    return render(request, 'tweet.html', {'form': form})


def main(request):
    data = Tweet.objects.all()
    return render(request, 'main.html', {'data': data})


def profile(request):
    myprofile = TwitterUser.objects.get(id=request.user.id)  # my profile id
    mymessages = Tweet.objects.filter(
        this_user=myprofile.id).order_by('-created_at')  # get's all my tweets
    return render(request, 'profile.html', {'mymessages': mymessages,
                                            "myprofile": myprofile})

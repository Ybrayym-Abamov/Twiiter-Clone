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
                        notified_tweet=messagebox,
                        target_user=target
                    )
        return HttpResponseRedirect(reverse('homepage'))
    form = TweetForm()
    return render(request, 'tweet.html', {'form': form})


@login_required
def main(request):
    # get's all of my tweets, which is just a query set
    tweets = Tweet.objects.filter(this_user=request.user)
    notif_count = Notification.objects.filter(
        target_user=request.user).filter(tweet_visibility=True).count()
    # for looping over my following query set
    for follower in request.user.following.all():
        # extending my initial tweets query set
        # by adding the tweets of the people I follow
        # the loop keeps running but everytime I run it new tweet of a user
        # get's added to my tweets query set that I'm displaying on the
        # my main page
        tweets = tweets | Tweet.objects.filter(this_user=follower)
    return render(request, 'main.html', {
        'tweets': tweets.order_by('-created_at'),
        'notif_count': notif_count})


def profile(request, username):
    html = 'profile.html'
    # get's my profile ID
    myprofile = TwitterUser.objects.get(id=request.user.id)
    # get's an ID of a user
    twitteruser = TwitterUser.objects.get(username=username)
    # get's the total number of a user's tweets
    number_of_tweets = Tweet.objects.filter(this_user=twitteruser).count()
    # get's the total number of accounts being followed
    numbder_of_following = twitteruser.following.count()-1  # subtracting to avoid "following yourself" bug is a bad practice
    # get's all of the user's tweets
    usertweets = Tweet.objects.filter(
        this_user=twitteruser).order_by('-created_at')
    context = {
        'myprofile': myprofile,
        'twitteruser': twitteruser,
        'usertweets': usertweets,
        'number_of_tweets': number_of_tweets,
        'numbder_of_following': numbder_of_following
    }
    return render(request, html, context)


def tweet_detail(request, id):
    data = Tweet.objects.get(id=id)
    return render(request, 'tweet_detail.html', {'data': data})


def user_detail(request, id):
    if request.user.is_authenticated:
        if request.user.id == id:
            return HttpResponseRedirect(reverse('profile',
                                        kwargs={
                                            'username': request.user.username})
                                        )
        user = TwitterUser.objects.get(id=id)
        following_number = user.following.count()
        tweet = Tweet.objects.filter(this_user=TwitterUser.objects.get(id=id))

        following_list = request.user.following.all()

        return render(request, 'user_detail.html', {
            'user': user,
            'tweet': tweet,
            'following_number': following_number,
            'following_list': following_list})
    else:  # if the user isn't authenticated
        user = TwitterUser.objects.get(id=id)
        following_number = user.following.count()
        tweet = Tweet.objects.filter(this_user=TwitterUser.objects.get(id=id))

        return render(request, 'user_detail.html', {
            'user': user,
            'tweet': tweet,
            'following_number': following_number})

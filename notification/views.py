from django.shortcuts import render, reverse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from notification.models import Notification
from twitteruser.models import TwitterUser


@login_required
def notif(request, username):
    notif_count = Notification.objects.filter(
        target_user=request.user).filter(tweet_visibility=True).count()
    actual_notifs = Notification.objects.filter(
        target_user=request.user).filter(tweet_visibility=True)
    for notif in actual_notifs:
        notif.tweet_visibility = False
        notif.save()
    return render(request, 'notifications.html', {
        'actual_notifs': actual_notifs,
        'notif_count': notif_count})

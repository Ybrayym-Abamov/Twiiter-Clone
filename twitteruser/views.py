from django.shortcuts import reverse, render, HttpResponseRedirect, redirect
from twitteruser.models import TwitterUser
from django.contrib.auth.decorators import login_required


@login_required
def follow(request, id):
    request.user.following.add(
        TwitterUser.objects.get(id=id)
    )
    return HttpResponseRedirect(reverse('userdetail', kwargs={'id': id}))


@login_required
def unfollow(request, id):
    request.user.following.remove(
        TwitterUser.objects.get(id=id)
    )
    return HttpResponseRedirect(reverse('userdetail', kwargs={'id': id}))

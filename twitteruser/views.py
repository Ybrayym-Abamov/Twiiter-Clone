from django.shortcuts import reverse, HttpResponseRedirect
from twitteruser.models import TwitterUser
from django.contrib.auth.decorators import login_required


@login_required
def follow(request, id):
    request.user.following.add(
        TwitterUser.objects.get(id=id)
    )
    return HttpResponseRedirect(reverse('homepage'))


@login_required
def unfollow(request, id):
    request.user.following.remove(
        TwitterUser.objects.get(id=id)
    )
    return HttpResponseRedirect(reverse('homepage'))

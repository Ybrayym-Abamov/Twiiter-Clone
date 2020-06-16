from django.shortcuts import render, reverse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from notification.models import Notification


@login_required
def notif(request):
    notif_count = Notification.objects.filter(target_user=request.user).count()
    

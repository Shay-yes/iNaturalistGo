"""
iNaturalist_447 Views

This file shows the html page to the user based on the url

Note: this may be moved to a separate directory when more views are developed.

"""

from django.shortcuts import render
# from django.conf import settings
# from django.shortcuts import redirect
# from django.contrib.auth.views import login
# from django.http import HttpResponse


# This shows the homepage when a user goes to the default url
def home(request):
    if request.user.is_authenticated:
        return render(request, 'home/user_home.html')
    else:
        return render(request, 'home/home_backup.html')

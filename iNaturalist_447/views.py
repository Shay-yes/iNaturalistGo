"""
iNaturalist_447 Views

This file shows the html page to the user based on the url

Note: this may be moved to a separate directory when more views are developed.

"""

from django.shortcuts import render


# from django.http import HttpResponse


# This shows the homepage when a user goes to the default url
def home(request):
    return render(request, 'home.html')

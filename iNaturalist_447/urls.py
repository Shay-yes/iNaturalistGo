"""iNaturalist_447 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from . import views
from django.contrib import admin
from django.urls import path, include
from users import views as user_views
from species import views as species_views
from django.conf import settings
from django.conf.urls.static import static

# These are the paths for each url
urlpatterns = [
    path('', views.home, name='home'),
    path('admin/', admin.site.urls),
    path('register/', user_views.register, name='register'),
    path('login/', user_views.login, name='login'),
    path('logout/', user_views.logout, name='logout'),
    path('accounts/', include('allauth.urls')),
    path('speciesUpload/', species_views.submit_view, name = 'species_upload'),
    path('gallery/', species_views.gallery_view, name = 'species_gallery'),
    path('googlec9d04339c6f2434c.html/', views.google_verify, name='google_verify'),
    path('accounts/profile/', views.profile_view, name='account_profile'),
    path('accounts/email/', views.email, name='email'),
    path('accounts/verification_sent/', views.verification_sent, name='verification_sent'),
    path('accounts/verified_email_required/', views.verified_email_required, name='verified_email_required'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

# Create your models here.
class Species(models.Model):
	# if user is deleted, we delete the species
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    common_name = models.CharField("Common name (if known)", max_length=50)
    latin_name = models.CharField("Latin name (if known)", max_length=50)
    location = models.CharField("Location (optional)", max_length=50, blank=True, default='')
    image = models.ImageField(default="default.jpg", upload_to='species_pics')

    def __str__(self):
        return self.common_name

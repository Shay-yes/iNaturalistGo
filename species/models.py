from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Species(models.Model):
	# if user is deleted, we delete the species
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	common_name = models.CharField(max_length=50)
	latin_name = models.CharField(max_length=50)
	image = models.ImageField(default="default.jpg", upload_to='species_pics')
	
	def __str__(self):
		return self.common_name

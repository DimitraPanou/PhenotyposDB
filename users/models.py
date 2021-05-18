from django.db import models
from django.contrib.auth.models import User
from PIL import Image

from assays.models import Facility

class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	facility = models.ForeignKey(Facility, models.DO_NOTHING,blank=True, null=True)
	first_name = models.CharField(max_length=256, blank=True, null=True)
	last_name = models.CharField(max_length=256, blank=True, null=True)
	internal_phone = models.CharField(max_length=16, blank=True, null=True)
	phone_number = models.CharField(max_length=16, blank=True, null=True)
	address_1 = models.CharField(max_length=256, blank=True, null=True)
	address_2 = models.CharField(max_length=256, blank=True, null=True)
	city = models.CharField(max_length=256, blank=True, null=True)
	state = models.CharField(max_length=256, blank=True, null=True)
	postal_code = models.IntegerField(blank=True, null=True)
	image = models.ImageField(default='default.png', upload_to='profile_pics')
	
	def __str__(self):
		return self.user.username+ ' Profile'

	def save(self, *args, **kwargs):
		super().save(*args, **kwargs)
		img = Image.open(self.image.path)
		
		if img.height > 300 or img.width > 300:
			output_size = (300, 300)
			img.thumbnail(output_size)
			img.save(self.image.path)

'''
	@property
	def get_first_name(self)
		if self.first_name:
			return self.first_name
		else:
			return ""
	@property
	def get_last_name(self)
		if self.last_name:
			return self.last_name
		else:
			return ""
	@property
	def get_first_name(self)
		if self.first_name:
			return self.first_name
		else:
			return ""
	@property
	def get_first_name(self)
		if self.first_name:
			return self.first_name
		else:
			return ""
	@property
	def get_first_name(self)
		if self.first_name:
			return self.first_name
		else:
			return ""
			'''
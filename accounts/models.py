from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _


class UserProfile(models.Model):
	user=models.OneToOneField(User,on_delete=models.CASCADE,related_name="profile")
	address=models.TextField(blank=True,null=True)
	phone=models.CharField(max_length=30,blank=True)
	date_joined=models.DateTimeField(auto_now_add=True)
	updated_on=models.DateTimeField(auto_now=True)
	is_creator=models.BooleanField(default=False)

	class Meta:
		db_table = 'UserProfile'
		verbose_name = _('user profile')
		verbose_name_plural = _('user profiles')
		ordering = ['-date_joined']

	def __str__(self):
		return self.user.username

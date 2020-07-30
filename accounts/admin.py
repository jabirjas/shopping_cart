from django.contrib import admin
from accounts.models import UserProfile
from django.contrib.auth.models import User


admin.site.register(UserProfile)

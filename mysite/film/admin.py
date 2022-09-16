from django.contrib import admin
from django.contrib.auth.models import User
from .models import Film
from .models import Comments


admin.site.register(Film)
admin.site.register(Comments)

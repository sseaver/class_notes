from django.contrib import admin
from menu.models import Special, Profile

# Register your models here.
admin.site.register([Special, Profile])

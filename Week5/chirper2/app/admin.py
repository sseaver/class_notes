from django.contrib import admin
from app.models import Chirp, Vote

# Register your models here.

admin.site.register([Chirp, Vote])

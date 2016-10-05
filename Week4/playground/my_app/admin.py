from django.contrib import admin
from my_app.models import Person, Team
# Register your models here.
admin.site.register([Person, Team])

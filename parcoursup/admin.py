from django.contrib import admin
from .models import Establishments, Formations, Applications

admin.site.register(Establishments)
admin.site.register(Formations)
admin.site.register(Applications)

# Register your models here.
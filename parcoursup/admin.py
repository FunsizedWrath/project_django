from django.contrib import admin
from .models import Establishments, Formations, Applications, Offers

admin.site.register(Establishments)
admin.site.register(Formations)
admin.site.register(Applications)
admin.site.register(Offers)

# Register your models here.
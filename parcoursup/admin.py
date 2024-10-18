from django.contrib import admin
from .models import Establishment
from .models import Formation
from .models import Application
from .models import hasFormation

admin.site.register(Establishment)
admin.site.register(Formation)
admin.site.register(Application)
admin.site.register(hasFormation)

# Register your models here.

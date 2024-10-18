from django.contrib import admin
from .models import Establishment, Formation, Application, Offers

admin.site.register(Establishment)
admin.site.register(Formation)
admin.site.register(Application)
admin.site.register(Offers)

# Register your models here.

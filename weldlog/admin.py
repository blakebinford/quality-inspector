from django.contrib import admin

from .models import Welder, Weld, Wps, Project, Nde, Drawings

# Register your models here.

admin.site.register(Weld)
admin.site.register(Welder)
admin.site.register(Wps)
admin.site.register(Project)
admin.site.register(Nde)
admin.site.register(Drawings)

from django.contrib import admin

from .models import Organization, District, Temperature


admin.site.register(Organization)
admin.site.register(District)
admin.site.register(Temperature)
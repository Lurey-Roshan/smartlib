from django.contrib import admin

# Register your models here.

from about.models import AboutUS, OurTeam,OurCient


admin.site.register(AboutUS)
admin.site.register(OurTeam)
admin.site.register(OurCient)
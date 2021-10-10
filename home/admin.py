from django.contrib import admin

# Register your models here.
from home.models import About_Us, Mission,Program, Message_from_Principal, Contact

admin.site.register(About_Us)
admin.site.register(Message_from_Principal)
admin.site.register(Mission)
admin.site.register(Program)
admin.site.register(Contact)
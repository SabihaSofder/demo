from django.contrib import admin
from .models import contactUs

# Register your models here.
class contactUsAdmin(admin.ModelAdmin):
    list_display = ('contactFullName', 'contactEmail', 'contactPhoneNumber', 'contactSubject', 'contactMessage')

admin.site.register(contactUs, contactUsAdmin)
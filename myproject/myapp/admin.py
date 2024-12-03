from django.contrib import admin
from .models import *

# Register your models here.
class contact_admin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'phone_number')  # Columns to display in the list view
    

# Register the model with the custom ModelAdmin
admin.site.register(contact, contact_admin)
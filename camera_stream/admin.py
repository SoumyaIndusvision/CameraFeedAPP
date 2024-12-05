from django.contrib import admin
from .models import Camera

# Registering the Camera model to the admin site
@admin.register(Camera)
class CameraAdmin(admin.ModelAdmin):
    list_display = ('name', 'ip_address', 'port', 'username', 'protocol')  # Fields to display in the list view
    search_fields = ('name', 'ip_address', 'username')  # Fields to search by in the admin interface
    list_filter = ('protocol',)  # Filters for protocol type
    ordering = ('name',)  # Default ordering by camera name

    # Optional: Customize the fieldsets to organize the admin form
    fieldsets = (
        (None, {
            'fields': ('name', 'ip_address', 'port', 'username', 'password')
        }),
        ('Advanced options', {
            'classes': ('collapse',),
            'fields': ('protocol',),
        }),
    )

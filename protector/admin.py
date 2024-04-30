from django.contrib import admin
from . import models

# Register your models here.

admin.site.site_header = "ShieldGuard Administration"
admin.site.site_title = 'ShieldGuard Site'


class ClientsMessagesAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone', 'email']


admin.site.register(models.ClientsMessages, ClientsMessagesAdmin)

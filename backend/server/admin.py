from django.contrib import admin
from .models import Server

class ServerAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'completed')
# Register your models here.

admin.site.register(Server, ServerAdmin)

from django.contrib import admin
from .models import Servers


class ServersAdmin(admin.ModelAdmin):
    def __init__(self, *args):
        super(ServersAdmin, self).__init__(*args)

    list_display = ['server_name', 'url', 'port', 'description']
    list_filter = ['server_name', ]
    search_fields = ['server_name', 'url', 'port', 'description']


admin.site.register(Servers, ServersAdmin)

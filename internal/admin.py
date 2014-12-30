from django.contrib import admin

from internal.models import Project, Client, Contact, \
     Website, Hours, Invoice

# Register your models here.
admin.site.register(Project)
admin.site.register(Client)
admin.site.register(Contact)
admin.site.register(Website)
admin.site.register(Hours)
admin.site.register(Invoice)
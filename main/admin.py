from django.contrib import admin

from main.models import Example, Trait, Contact

# Register your models here.
admin.site.register(Example)
admin.site.register(Trait)
admin.site.register(Contact)
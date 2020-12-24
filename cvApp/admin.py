from django.contrib import admin
from .models import Certif, Contact

# Register your models here.
class searchAdmin(admin.ModelAdmin):
    search_fields = ('Name',)

admin.site.register(Certif, searchAdmin)
admin.site.register(Contact)
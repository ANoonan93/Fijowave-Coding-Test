from django.contrib import admin

# Register your models here.
from .models import Machines

class machineSearch(admin.ModelAdmin):
	list_display = ('id', 'version')
	search_fields = ['id', 'version',]

admin.site.register(Machines, machineSearch)
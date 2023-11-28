from django.contrib import admin
from .models import Teachers, Vendors, Wallet, Calendar, Menu

# Register your models here.
admin.site.register(Teachers)
admin.site.register(Vendors)
admin.site.register(Wallet)
admin.site.register(Calendar)
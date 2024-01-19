from django.contrib import admin
from .models import order

class OrderAdmin(admin.ModelAdmin):
    list_display=('name','email','phone','food','address','add_date')
    search_fields=('name',)
    list_filter=('food',)

# Register your models here.
admin.site.site_header="Hungerite Admin"
admin.site.site_title="Hungerite Admin Panel"
admin.site.index_title="Welcome to Hungerite Admin Panel"
admin.site.register(order,OrderAdmin)
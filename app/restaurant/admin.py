from django.contrib import admin

# Register your models here.
from restaurant.models import Restaurant


class RestaurantAdmin(admin.ModelAdmin):
    pass
admin.site.register(Restaurant, RestaurantAdmin)
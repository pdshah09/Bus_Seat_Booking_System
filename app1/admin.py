from django.contrib import admin

from .models import  Register, BusDetail, Seat,Route


class RouteAdmin(admin.ModelAdmin):
        model=Route
        list_display=['bus','Location','marked']
admin.site.register(Register)
admin.site.register(Seat)
admin.site.register(BusDetail)
admin.site.register(Route,RouteAdmin)

admin.site.site_header = 'Bus Monitoring Panel'                  
admin.site.index_title = 'Features area'                 
admin.site.site_title = 'Bus Monitoring adminsitration'


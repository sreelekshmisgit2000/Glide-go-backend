# planner/admin.py
from django.contrib import admin
from .models import *

admin.site.register(Location)
admin.site.register(Hotel)
admin.site.register(CabType)
admin.site.register(BudgetRange)
admin.site.register(DaysOption)
admin.site.register(MembersOption)
admin.site.register(ChildrenOption)
admin.site.register(RoomsOption)
admin.site.register(CabCategory)
admin.site.register(Vehicle)
admin.site.register(VehicleImage)
admin.site.register(Driver)
admin.site.register(DriverImage)
admin.site.register(Cab)
admin.site.register(Destination)
admin.site.register(Place)
admin.site.register(PlaceImage)
admin.site.register(Activity)
admin.site.register(Country)
admin.site.register(Page)

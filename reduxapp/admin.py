from django.contrib import admin
from .models import *





# Classifier Models
admin.site.register(HotelCategory)
admin.site.register(RoomType)
admin.site.register(DocumentType)
admin.site.register(ActivityType)

# Main Models
admin.site.register(Amenity)
admin.site.register(Activity)
admin.site.register(HotelDocument)
admin.site.register(Driver)
admin.site.register(Cab)
admin.site.register(Plan)
admin.site.register(Hotel)

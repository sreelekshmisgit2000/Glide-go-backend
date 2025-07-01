# views/__init__.py

# Location
from .locations import LocationViewSet

# Driver
from .drivers import DriversViewSet

# Hotel
from .hotels import HotelViewSet

# Cab-related
from .cabs import CabTypeViewSet, CabViewSet, CabCategoryViewSet

# Budget
from .budget import BudgetRangeViewSet

# Option fields


# Images
from .images import (
    DriverImageListCreateView,
    DriverImageDeleteView,
    DriverImageGroupedView,
    VehicleImageViewSet,
    VehicleImageGroupedViewSet,
    VehicleImageDeleteView,
    
)



# Destinations
from .destinations import DestinationViewSet

# Places
from .places import PlaceViewSet, PlaceImageViewSet

# Users
from .users import CurrentUserAPIView

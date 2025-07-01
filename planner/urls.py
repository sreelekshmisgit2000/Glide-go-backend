from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from planner.views.cabs import CabViewSet
from planner.views.activity import ActivityViewSet
from planner.views.budget import BudgetRangeViewSet
from planner.views.cabs import CabCategoryViewSet
from planner.views.destinations import DestinationViewSet
from planner.views.drivers import DriversViewSet
from planner.views.hotels import HotelViewSet
from planner.views.images import DriverImageDeleteView, DriverImageGroupedView, DriverImageListCreateView, VehicleImageDeleteView, VehicleImageGroupedViewSet, VehicleImageViewSet
from planner.views.locations import LocationViewSet
from planner.views.places import PlaceImageViewSet, PlaceImagesGroupedView, PlaceViewSet
from planner.views.users import CurrentUserAPIView
from planner.views.vehicles import VehicleViewSet


urlpatterns = [
    # JWT Auth
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("users/me/", CurrentUserAPIView.as_view(), name="users-me"),

    # Main API Views
    path("locations/", LocationViewSet.as_view({'get': 'list', 'post': 'create'})),
    path("locations/<int:pk>/", LocationViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),

    path("drivers/", DriversViewSet.as_view({'get': 'list', 'post': 'create'})),
    path("drivers/<int:pk>/", DriversViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),

    path("hotels/", HotelViewSet.as_view({'get': 'list', 'post': 'create'})),
    path("hotels/<int:pk>/", HotelViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),

    path("cabs/", CabViewSet.as_view({'get': 'list', 'post': 'create'})),
    path("cabs/<int:id>/", CabViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),

    path("destinations/", DestinationViewSet.as_view({'get': 'list', 'post': 'create'})),
    path("destinations/<int:id>/", DestinationViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),

    path("cab-categories/", CabCategoryViewSet.as_view({'get': 'list', 'post': 'create'})),
    path("cab-categories/<int:id>/", CabCategoryViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),

    path("budget-ranges/", BudgetRangeViewSet.as_view({'get': 'list'})), 
path("budget-ranges/<int:pk>/", BudgetRangeViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy',
})),

 
  
    path("vehicles/", VehicleViewSet.as_view({'get': 'list', 'post': 'create'})),
    path("vehicles/<int:id>/", VehicleViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),
    path("places/", PlaceViewSet.as_view({'get': 'list', 'post': 'create'})),
    path("places/<int:id>/", PlaceViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),
    path("place-images/", PlaceImageViewSet.as_view({'get': 'list', 'post': 'create'})),
    path("place-images/<int:id>/", PlaceImageViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),
    path("activities/", ActivityViewSet.as_view({'get': 'list', 'post': 'create'})),
    path("activities/<int:id>/", ActivityViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),
    path("cab-categories-list/", CabCategoryViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name="cab-categories-list"),
    path("budget-ranges/", BudgetRangeViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name="budget-ranges"),
    path("vehicle-list/", VehicleViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name="vehicle-list"),
    path("destination-list-create/", DestinationViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name="destination-list-create"),
    path('driver-images/', DriverImageListCreateView.as_view(), name='driver-image-upload'),
    path('driver-images/<int:pk>/', DriverImageDeleteView.as_view(), name='driver-image-delete'),
    path('driver-images-grouped/', DriverImageGroupedView.as_view(), name='driver-images-grouped'),
    path("place-images/", PlaceImageViewSet.as_view({'post': 'create'})),
    path("place-images/<int:pk>/", PlaceImageViewSet.as_view({'delete': 'destroy'})),
    path("place-images-grouped/", PlaceImagesGroupedView.as_view()),
 path("vehicle-images/", VehicleImageViewSet.as_view({'get': 'list', 'post': 'create'})),
    path("vehicle-images/<int:pk>/", VehicleImageDeleteView.as_view()),
    path("vehicle-images-grouped/", VehicleImageGroupedViewSet.as_view({'get': 'list'})),
]

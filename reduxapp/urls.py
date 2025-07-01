from django.urls import path
from .views import *


urlpatterns = [
    # --- Plans ---
    path('plans/', PlanView.as_view(), name='plans'),
    path('plans/<str:plan_id>/', PlanDetailView.as_view(), name='plan-detail'),

    # --- Core Features ---
    path('hotels/', ApprovedHotelsView.as_view(), name='approved-hotels'),
    path('activities/', ActivityListView.as_view(), name='activities'),
    path('cabs/', VerifiedCabListView.as_view(), name='verified-cabs'),

    # --- Classifiers (optional) ---
    path('classifiers/hotel-categories/', HotelCategoryListView.as_view(), name='hotel-categories'),
    path('classifiers/room-types/', RoomTypeListView.as_view(), name='room-types'),
    path('classifiers/document-types/', DocumentTypeListView.as_view(), name='document-types'),
    path('classifiers/activity-types/', ActivityTypeListView.as_view(), name='activity-types'),
]
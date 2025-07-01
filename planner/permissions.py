from rest_framework.permissions import BasePermission

# ----------- Location Permissions -----------
class CanView_Location(BasePermission):
    def has_permission(self, request, view):
        return request.user.has_perm('planner.view_location')

class CanAdd_Location(BasePermission):
    def has_permission(self, request, view):
        return request.user.has_perm('planner.add_location')

class CanChange_Location(BasePermission):
    def has_permission(self, request, view):
        return request.user.has_perm('planner.change_location')

class CanDelete_Location(BasePermission):
    def has_permission(self, request, view):
        return request.user.has_perm('planner.delete_location')


# ----------- Hotel Permissions -----------
class CanView_Hotel(BasePermission):
    def has_permission(self, request, view):
        
        return request.user.has_perm('planner.view_hotels')

class CanAdd_Hotel(BasePermission):
    def has_permission(self, request, view):
        return request.user.has_perm('planner.add_hotels')

class CanChange_Hotel(BasePermission):
    def has_permission(self, request, view):
        return request.user.has_perm('planner.change_hotels')

class CanDelete_Hotel(BasePermission):
    def has_permission(self, request, view):
        return request.user.has_perm('planner.delete_hotels')


# ----------- CabType Permissions -----------
class CanView_Cabtype(BasePermission):
    def has_permission(self, request, view):
        
        return request.user.has_perm('planner.view_cabtype')

class CanAdd_Cabtype(BasePermission):
    def has_permission(self, request, view):
        return request.user.has_perm('planner.add_cabtype')

class CanChange_Cabtype(BasePermission):
    def has_permission(self, request, view):
        return request.user.has_perm('planner.change_cabtype')

class CanDelete_Cabtype(BasePermission):
    def has_permission(self, request, view):
        return request.user.has_perm('planner.delete_cabtype')


# ----------- BudgetRange Permissions -----------
class CanView_Budgetrange(BasePermission):
    def has_permission(self, request, view):
        return request.user.has_perm('planner.view_budgetrange')

class CanAdd_Budgetrange(BasePermission):
    def has_permission(self, request, view):
        return request.user.has_perm('planner.add_budgetrange')

class CanChange_Budgetrange(BasePermission):
    def has_permission(self, request, view):
        return request.user.has_perm('planner.change_budgetrange')

class CanDelete_Budgetrange(BasePermission):
    def has_permission(self, request, view):
        return request.user.has_perm('planner.delete_budgetrange')
    
class CanView_DriverImagesGroup(BasePermission):
    def has_permission(self, request, view):
        return request.user.has_perm('planner.view_driverimagesgroup')


# ----------- DaysOption Permissions -----------
class CanView_Daysoption(BasePermission):
    def has_permission(self, request, view):
        return request.user.has_perm('planner.view_daysoption')

class CanAdd_Daysoption(BasePermission):
    def has_permission(self, request, view):
        return request.user.has_perm('planner.add_daysoption')

class CanChange_Daysoption(BasePermission):
    def has_permission(self, request, view):
        return request.user.has_perm('planner.change_daysoption')

class CanDelete_Daysoption(BasePermission):
    def has_permission(self, request, view):
        return request.user.has_perm('planner.delete_daysoption')


# ----------- MembersOption Permissions -----------
class CanView_Membersoption(BasePermission):
    def has_permission(self, request, view):
        return request.user.has_perm('planner.view_membersoption')

class CanAdd_Membersoption(BasePermission):
    def has_permission(self, request, view):
        return request.user.has_perm('planner.add_membersoption')

class CanChange_Membersoption(BasePermission):
    def has_permission(self, request, view):
        return request.user.has_perm('planner.change_membersoption')

class CanDelete_Membersoption(BasePermission):
    def has_permission(self, request, view):
        return request.user.has_perm('planner.delete_membersoption')


# ----------- ChildrenOption Permissions -----------
class CanView_Childrenoption(BasePermission):
    def has_permission(self, request, view):
        return request.user.has_perm('planner.view_childrenoption')

class CanAdd_Childrenoption(BasePermission):
    def has_permission(self, request, view):
        return request.user.has_perm('planner.add_childrenoption')

class CanChange_Childrenoption(BasePermission):
    def has_permission(self, request, view):
        return request.user.has_perm('planner.change_childrenoption')

class CanDelete_Childrenoption(BasePermission):
    def has_permission(self, request, view):
        return request.user.has_perm('planner.delete_childrenoption')


# ----------- RoomsOption Permissions -----------
class CanView_Roomsoption(BasePermission):
    def has_permission(self, request, view):
        return request.user.has_perm('planner.view_roomsoption')

class CanAdd_Roomsoption(BasePermission):
    def has_permission(self, request, view):
        return request.user.has_perm('planner.add_roomsoption')

class CanChange_Roomsoption(BasePermission):
    def has_permission(self, request, view):
        return request.user.has_perm('planner.change_roomsoption')

class CanDelete_Roomsoption(BasePermission):
    def has_permission(self, request, view):
        return request.user.has_perm('planner.delete_roomsoption')


# ----------- CabCategory Permissions -----------
class CanView_CabcategorY(BasePermission):
    def has_permission(self, request, view):
        
        return request.user.has_perm('planner.view_cabcategory')

class CanAdd_CabcategorY(BasePermission):
    def has_permission(self, request, view):
        return request.user.has_perm('planner.add_cabcategorY')

class CanChange_CabcategorY(BasePermission):
    def has_permission(self, request, view):
        return request.user.has_perm('planner.change_cabcategorY')

class CanDelete_CabcategorY(BasePermission):
    def has_permission(self, request, view):
        return request.user.has_perm('planner.delete_cabcategorY')

# ----------- Vehicle Permissions -----------
class CanView_Vehicle(BasePermission):
    def has_permission(self, request, view):
        return request.user.has_perm('planner.view_vehicle')

class CanAdd_Vehicle(BasePermission):
    def has_permission(self, request, view):
        return request.user.has_perm('planner.add_vehicle')

class CanChange_Vehicle(BasePermission):
    def has_permission(self, request, view):
        return request.user.has_perm('planner.change_vehicle')

class CanDelete_Vehicle(BasePermission):
    def has_permission(self, request, view):
        return request.user.has_perm('planner.delete_vehicle')


# ----------- VehicleImage Permissions -----------
class CanView_Vehicleimage(BasePermission):
    def has_permission(self, request, view):
        return request.user.has_perm('planner.view_vehicleimage')

class CanAdd_Vehicleimage(BasePermission):
    def has_permission(self, request, view):
        return request.user.has_perm('planner.add_vehicleimage')

class CanChange_Vehicleimage(BasePermission):
    def has_permission(self, request, view):
        return request.user.has_perm('planner.change_vehicleimage')

class CanDelete_Vehicleimage(BasePermission):
    def has_permission(self, request, view):
        return request.user.has_perm('planner.delete_vehicleimage')


# ----------- Driver Permissions -----------
class CanView_Driver(BasePermission):
    def has_permission(self, request, view):
        return request.user.has_perm('planner.view_drivers')

class CanAdd_Driver(BasePermission):
    def has_permission(self, request, view):
        return request.user.has_perm('planner.add_drivers')

class CanChange_Driver(BasePermission):
    def has_permission(self, request, view):
        return request.user.has_perm('planner.change_drivers')

class CanDelete_Driver(BasePermission):
    def has_permission(self, request, view):
        return request.user.has_perm('planner.delete_drivers')


# ----------- DriverImage Permissions -----------
class CanView_Driverimage(BasePermission):
    def has_permission(self, request, view):
        return request.user.has_perm('planner.view_driverimage')

class CanAdd_Driverimage(BasePermission):
    def has_permission(self, request, view):
        return request.user.has_perm('planner.add_driverimage')

class CanChange_Driverimage(BasePermission):
    def has_permission(self, request, view):
        return request.user.has_perm('planner.change_driverimage')

class CanDelete_Driverimage(BasePermission):
    def has_permission(self, request, view):
        return request.user.has_perm('planner.delete_driverimage')


# ----------- Cab Permissions -----------
class CanView_Cab(BasePermission):
    def has_permission(self, request, view):
        return request.user.has_perm('planner.view_cab')

class CanAdd_Cab(BasePermission):
    def has_permission(self, request, view):
        return request.user.has_perm('planner.add_cab')

class CanChange_Cab(BasePermission):
    def has_permission(self, request, view):
        return request.user.has_perm('planner.change_cab')

class CanDelete_Cab(BasePermission):
    def has_permission(self, request, view):
        return request.user.has_perm('planner.delete_cab')


# ----------- Destination Permissions -----------
class CanView_Destination(BasePermission):
    def has_permission(self, request, view):
        return request.user.has_perm('planner.view_destination')

class CanAdd_Destination(BasePermission):
    def has_permission(self, request, view):
        return request.user.has_perm('planner.add_destination')

class CanChange_Destination(BasePermission):
    def has_permission(self, request, view):
        return request.user.has_perm('planner.change_destination')

class CanDelete_Destination(BasePermission):
    def has_permission(self, request, view):
        return request.user.has_perm('planner.delete_destination')


# ----------- Place Permissions -----------
class CanView_Place(BasePermission):
    def has_permission(self, request, view):
        return request.user.has_perm('planner.view_place')

class CanAdd_Place(BasePermission):
    def has_permission(self, request, view):
        return request.user.has_perm('planner.add_place')

class CanChange_Place(BasePermission):
    def has_permission(self, request, view):
        return request.user.has_perm('planner.change_place')

class CanDelete_Place(BasePermission):
    def has_permission(self, request, view):
        return request.user.has_perm('planner.delete_place')


# ----------- PlaceImage Permissions -----------
class CanView_Placeimage(BasePermission):
    def has_permission(self, request, view):
        return request.user.has_perm('planner.view_placeimage')

class CanAdd_Placeimage(BasePermission):
    def has_permission(self, request, view):
        return request.user.has_perm('planner.add_placeimage')

class CanChange_Placeimage(BasePermission):
    def has_permission(self, request, view):
        return request.user.has_perm('planner.change_placeimage')

class CanDelete_Placeimage(BasePermission):
    def has_permission(self, request, view):
        return request.user.has_perm('planner.delete_placeimage')


# ----------- Activity Permissions -----------
class CanView_Activity(BasePermission):
    def has_permission(self, request, view):
        return request.user.has_perm('planner.view_activities')

class CanAdd_Activity(BasePermission):
    def has_permission(self, request, view):
        return request.user.has_perm('planner.add_activities')

class CanChange_Activity(BasePermission):
    def has_permission(self, request, view):
        return request.user.has_perm('planner.change_activities')

class CanDelete_Activity(BasePermission):
    def has_permission(self, request, view):
        return request.user.has_perm('planner.delete_activities')


# ----------- Country Permissions -----------
class CanView_Country(BasePermission):
    def has_permission(self, request, view):
        return request.user.has_perm('planner.view_country')

class CanAdd_Country(BasePermission):
    def has_permission(self, request, view):
        return request.user.has_perm('planner.add_country')

class CanChange_Country(BasePermission):
    def has_permission(self, request, view):
        return request.user.has_perm('planner.change_country')

class CanDelete_Country(BasePermission):
    def has_permission(self, request, view):
        return request.user.has_perm('planner.delete_country')


# ----------- TripRequest Permissions -----------
class CanView_Triprequest(BasePermission):
    def has_permission(self, request, view):
        return request.user.has_perm('planner.view_triprequest')

class CanAdd_Triprequest(BasePermission):
    def has_permission(self, request, view):
        return request.user.has_perm('planner.add_triprequest')

class CanChange_Triprequest(BasePermission):
    def has_permission(self, request, view):
        return request.user.has_perm('planner.change_triprequest')

class CanDelete_Triprequest(BasePermission):
    def has_permission(self, request, view):
        return request.user.has_perm('planner.delete_triprequest')


# ----------- TripPlan Permissions -----------
class CanView_Tripplan(BasePermission):
    def has_permission(self, request, view):
        return request.user.has_perm('planner.view_tripplan')

class CanAdd_Tripplan(BasePermission):
    def has_permission(self, request, view):
        return request.user.has_perm('planner.add_tripplan')

class CanChange_Tripplan(BasePermission):
    def has_permission(self, request, view):
        return request.user.has_perm('planner.change_tripplan')

class CanDelete_Tripplan(BasePermission):
    def has_permission(self, request, view):
        return request.user.has_perm('planner.delete_tripplan')


# ----------- Page Permissions -----------
class CanView_Page(BasePermission):
    def has_permission(self, request, view):
        return request.user.has_perm('planner.view_page')

class CanAdd_Page(BasePermission):
    def has_permission(self, request, view):
        return request.user.has_perm('planner.add_page')

class CanChange_Page(BasePermission):
    def has_permission(self, request, view):
        return request.user.has_perm('planner.change_page')

class CanDelete_Page(BasePermission):
    def has_permission(self, request, view):
        return request.user.has_perm('planner.delete_page')


# ----------- RolePermission Permissions -----------
class CanView_Rolepermission(BasePermission):
    def has_permission(self, request, view):
        return request.user.has_perm('planner.view_rolepermission')

class CanAdd_Rolepermission(BasePermission):
    def has_permission(self, request, view):
        return request.user.has_perm('planner.add_rolepermission')

class CanChange_Rolepermission(BasePermission):
    def has_permission(self, request, view):
        return request.user.has_perm('planner.change_rolepermission')

class CanDelete_Rolepermission(BasePermission):
    def has_permission(self, request, view):
        return request.user.has_perm('planner.delete_rolepermission')


class CanView_DriverImage(BasePermission):
    def has_permission(self, request, view):
        return request.user.has_perm('planner.view_driverimage')

class CanAdd_DriverImage(BasePermission):
    def has_permission(self, request, view):
        return request.user.has_perm('planner.add_driverimage')

class CanChange_DriverImage(BasePermission):
    def has_permission(self, request, view):
        return request.user.has_perm('planner.change_driverimage')

class CanDelete_DriverImage(BasePermission):
    def has_permission(self, request, view):
        return request.user.has_perm('planner.delete_driverimage')

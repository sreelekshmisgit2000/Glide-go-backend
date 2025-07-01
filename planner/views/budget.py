from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from planner.models import BudgetRange
from ..serializers import BudgetRangeSerializer
from planner.permissions import (
    CanView_Budgetrange, CanAdd_Budgetrange,
    CanChange_Budgetrange, CanDelete_Budgetrange
)

class BudgetRangeViewSet(viewsets.ModelViewSet):
    queryset = BudgetRange.objects.all()
    serializer_class = BudgetRangeSerializer

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            return [CanView_Budgetrange()]
        elif self.action == 'create':
            return [CanAdd_Budgetrange()]
        elif self.action in ['update', 'partial_update']:
            return [CanChange_Budgetrange()]
        elif self.action == 'destroy':
            return [CanDelete_Budgetrange()]
        return [IsAuthenticated()]

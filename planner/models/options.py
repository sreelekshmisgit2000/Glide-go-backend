from django.db import models

class BudgetRange(models.Model):
    min_price = models.IntegerField()
    max_price = models.IntegerField()
    def __str__(self): return f"{self.min_price} - {self.max_price}"

class DaysOption(models.Model):
    value = models.PositiveIntegerField()
    def __str__(self): return str(self.value)

# Same for MembersOption, ChildrenOption, RoomsOption

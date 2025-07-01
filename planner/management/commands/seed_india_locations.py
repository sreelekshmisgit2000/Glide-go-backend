# planner/management/commands/seed_trip_plans.py
from django.core.management.base import BaseCommand
from planner.models import  Location, Hotel, CabType, TripPlan

import random

class Command(BaseCommand):
    help = "Seed 100 sample TripPlans"

    def handle(self, *args, **kwargs):
        TripPlan.objects.all().delete()

        locations  = list(Location.objects.all())
        hotels     = list(Hotel.objects.all())
        cab_types  = list(CabType.objects.all())

        if len(locations) < 2 or not hotels or not cab_types:
            self.stdout.write(self.style.ERROR(
                "Seed Locations, Hotels, and CabTypes first."))
            return

        for i in range(100):                                           # ← 100 plans
            start = random.choice(locations)
            end   = random.choice([loc for loc in locations if loc != start])

            TripPlan.objects.create(
                name=f"Trip Plan {i+1}",
                description=f"Exciting journey from {start.name} to {end.name}.",
                start_location=start,
                end_location=end,
                hotel=random.choice(hotels),
                cab_type=random.choice(cab_types),
                days=random.randint(2, 7),
                base_price=random.randint(3000, 20000),
            )

        self.stdout.write(self.style.SUCCESS("✔ TripPlan seeding complete (100 entries)"))

import uuid

from django.core.management.base import BaseCommand
from places.models import Category, Place
from profiles.models import CustomUser, UserProfile
from trips.models import Trip


class Command(BaseCommand):
    help = "Seed the database with initial data"

    def add_arguments(self, parser):
        parser.add_argument(
            "--flush",
            action="store_true",
            help="Clear existing data before seeding",
        )

    def handle(self, *args, **options):
        if options["flush"]:
            self.stdout.write(self.style.WARNING("Flushing existing data..."))
            Trip.objects.all().delete()
            Place.objects.all().delete()
            Category.objects.all().delete()
            CustomUser.objects.all().delete()
            self.stdout.write(self.style.SUCCESS("  ✓ Flushed"))

        self._seed_categories()
        self._seed_places()
        self._seed_users()
        self._seed_trips()

        self.stdout.write(self.style.SUCCESS("\n✅ Seeding complete!"))
        self.stdout.write(f"   {Category.objects.count()} categories")
        self.stdout.write(f"   {Place.objects.count()} places")
        self.stdout.write(f"   {CustomUser.objects.count()} users")
        self.stdout.write(f"   {UserProfile.objects.count()} profiles")
        self.stdout.write(f"   {Trip.objects.count()} trips")

    def _seed_categories(self):
        self.stdout.write("Seeding categories...")
        self.categories = {}
        for name in ["Restaurant", "Hotel", "Museum", "Park", "Café"]:
            cat, created = Category.objects.get_or_create(name=name)
            self.categories[name] = cat
            self.stdout.write(f"  {'✓ Created' if created else '~ Exists'}: {cat.name}")

    def _seed_places(self):
        self.stdout.write("Seeding places...")
        places_data = [
            {
                "id": uuid.uuid4(),
                "name": "The French Laundry",
                "short_name": "French Laundry",
                "description": "World-renowned fine dining restaurant in Yountville, Napa Valley.",
                "category": self.categories["Restaurant"],
                "address": "6640 Washington St",
                "region": "California",
                "country": "US",
                "popularity": 0.98,
                "price": 4.0,
                "rating": 9.5,
                "email": "reservations@frenchlaundry.com",
                "telephone": "+1-707-944-2380",
                "website": "https://www.thomaskeller.com/tfl",
            },
            {
                "id": uuid.uuid4(),
                "name": "Central Park",
                "short_name": "Central Park",
                "description": "Iconic 843-acre urban park in the heart of Manhattan.",
                "category": self.categories["Park"],
                "address": "Central Park",
                "region": "New York",
                "country": "US",
                "popularity": 0.99,
                "price": 0.0,
                "rating": 9.3,
                "email": "info@centralparknyc.org",
                "telephone": "+1-212-310-6600",
                "website": "https://www.centralparknyc.org",
            },
            {
                "id": uuid.uuid4(),
                "name": "The Metropolitan Museum of Art",
                "short_name": "The Met",
                "description": "One of the world's largest and most visited art museums.",
                "category": self.categories["Museum"],
                "address": "1000 Fifth Ave",
                "region": "New York",
                "country": "US",
                "popularity": 0.97,
                "price": 2.0,
                "rating": 9.6,
                "email": "information@metmuseum.org",
                "telephone": "+1-212-535-7710",
                "website": "https://www.metmuseum.org",
            },
            {
                "id": uuid.uuid4(),
                "name": "Blue Bottle Coffee",
                "short_name": "Blue Bottle",
                "description": "Specialty coffee roaster known for single-origin brews.",
                "category": self.categories["Café"],
                "address": "300 Webster St",
                "region": "California",
                "country": "US",
                "popularity": 0.85,
                "price": 1.0,
                "rating": 8.7,
                "email": "hello@bluebottlecoffee.com",
                "telephone": "+1-510-653-3394",
                "website": "https://bluebottlecoffee.com",
            },
            {
                "id": uuid.uuid4(),
                "name": "The Ritz-Carlton",
                "short_name": "Ritz-Carlton",
                "description": "Luxury 5-star hotel with iconic service and amenities.",
                "category": self.categories["Hotel"],
                "address": "160 E Pearson St",
                "region": "Illinois",
                "country": "US",
                "popularity": 0.92,
                "price": 4.0,
                "rating": 9.1,
                "email": "chicago@ritzcarlton.com",
                "telephone": "+1-312-266-1000",
                "website": "https://www.ritzcarlton.com/chicago",
            },
        ]
        self.places = []
        for data in places_data:
            place, created = Place.objects.get_or_create(id=data["id"], defaults=data)
            self.places.append(place)
            self.stdout.write(f"  {'✓ Created' if created else '~ Exists'}: {place.name}")

    def _seed_users(self):
        self.stdout.write("Seeding users...")
        users_data = [
            {"username": "alice", "email": "alice@example.com", "password": "Password123!", "displayed_name": "Alice Wonder"},
            {"username": "bob",   "email": "bob@example.com",   "password": "Password123!", "displayed_name": "Bob Builder"},
            {"username": "carol", "email": "carol@example.com", "password": "Password123!", "displayed_name": "Carol Smith"},
        ]
        if not CustomUser.objects.filter(username="mctraher").exists():
            CustomUser.objects.create_superuser(
                username="mctraher",
                email= "mctraher@hochushmali.com",
                password="D1r1zhab!",
                is_active=True,
                is_staff=True,
                is_superuser=True,
            )

        self.users = []
        for data in users_data:
            user, created = CustomUser.objects.get_or_create(
                email=data["email"],
                defaults={"username": data["username"]},
            )
            if created:
                user.set_password(data["password"])
                user.save()
                user.profile.displayed_name = data["displayed_name"]
                user.profile.save()
            self.users.append(user)
            self.stdout.write(f"  {'✓ Created' if created else '~ Exists'}: {user.email}")
    def _seed_trips(self):
        self.stdout.write("Seeding trips...")
        trips_data = [
            {"places": [self.places[1], self.places[2]]},  # Central Park + The Met
            {"places": [self.places[0], self.places[3]]},  # French Laundry + Blue Bottle
            {"places": [self.places[4], self.places[0]]},  # Ritz-Carlton + French Laundry
        ]
        for data in trips_data:
            trip = Trip.objects.create()
            trip.places.set(data["places"])
            self.stdout.write(f"  ✓ Trip with {trip.places.count()} places")
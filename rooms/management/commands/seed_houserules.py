from django.core.management.base import BaseCommand
from rooms.models import HouseRule


class Command(BaseCommand):

    help = "This command creates amenities"

    """def add_arguments(self, parser):
        parser.add_argument(
            "--times",
            help="godclean",
        )"""

    def handle(self, *args, **options):
        houserules = [
            "No smoking",
            "No pets",
            "No parties or events",
            "Self check-in with keypad",
            "Not suitable for children and infants",
        ]
        for h in houserules:
            HouseRule.objects.create(name=h)
        self.stdout.write(self.style.SUCCESS(f"{len(houserules)} Houserules created."))

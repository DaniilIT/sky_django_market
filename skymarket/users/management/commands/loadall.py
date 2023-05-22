from django.core.management.base import BaseCommand
from django.core.management import call_command

from skymarket.settings import BASE_DIR


class Command(BaseCommand):
    help = "Loads fixtures from fixtures dir"
    fixtures_dir = BASE_DIR / "fixtures"
    loaddata_command = "loaddata"
    filenames = [
        "users",
        "ad",
        "comments",
    ]

    def handle(self, *args, **options):
        for fixture_filename in self.filenames:
            call_command(
                self.loaddata_command, self.fixtures_dir / f"{fixture_filename}.json"
            )

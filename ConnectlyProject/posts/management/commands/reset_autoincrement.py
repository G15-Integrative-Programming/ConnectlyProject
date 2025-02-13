from django.core.management.base import BaseCommand
from django.db import connection

class Command(BaseCommand):
    help = 'Reset AUTOINCREMENT counter for a specified table'

    def add_arguments(self, parser):
        parser.add_argument('table_name', type=str, help='Table name to reset the AUTOINCREMENT')

    def handle(self, *args, **options):
        table_name = options['table_name']

        try:
            with connection.cursor() as cursor:
                # Delete all rows (optional)
                cursor.execute(f"DELETE FROM {table_name}")
                # Reset the AUTOINCREMENT counter
                cursor.execute(f"DELETE FROM sqlite_sequence WHERE name='{table_name}'")

            self.stdout.write(self.style.SUCCESS(f"Auto-increment counter reset for {table_name}"))

        except Exception as e:
            self.stdout.write(self.style.ERROR(f"Error: {str(e)}"))

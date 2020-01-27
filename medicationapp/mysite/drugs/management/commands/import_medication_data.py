from django.core.management.base import BaseCommand
from drugs.models import Medication as Drug


class Command(BaseCommand):

    def handle(self, *args, **options):
        if options['import_medication_data']:
            print('Open file')
            open('medication_database.txt', 'r')

        else:
            print('Error: specify file')


    def add_arguments(self, parser):
        parser.add_argument(
            'import_medication_data',
            action='store_true',
            default=False,
            help='Imports medication data'
        )


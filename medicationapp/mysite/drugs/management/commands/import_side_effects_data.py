from django.core.management.base import BaseCommand
from drugs.models import Medication, SideEffect


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument(
            '--side_effects_data_file',
            help='Name of the file with medication side effects data'
        )


    def handle(self, *args, **options):
        side_effect_data_filename = options['side_effects_data_file']

        if side_effect_data_filename:
            content_lines = []

            with open(side_effect_data_filename, 'r') as f:
                next(f)
                content_lines = f.readlines()



            for row in content_lines:
                row = row.split(',')

                medicationName = row[0].strip()

                med = Medication.objects.filter(medication_name=medicationName).first()

                if not med:
                    print('error: can not find medication %s associated with side effect' % medicationName)
                    continue

                sideEffect = SideEffect()
                sideEffect.medication = med

        else:
            print('Error: specify file')
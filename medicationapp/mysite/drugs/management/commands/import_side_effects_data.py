from django.core.management.base import BaseCommand
from drugs.models import Medication, SideEffect


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument(
            '--side_effects_data_file',
            help='Name of the file with medication side effects data'
        )


    def handle(self, *args, **options):
        # get the name of the file to import from arguments
        side_effect_data_filename = options['side_effects_data_file']
        #if options['medication_data_file']:


        # if filename is not empty, open the file and read all lines
        if side_effect_data_filename:
            content_lines = []

            with open(side_effect_data_filename, 'r') as f:
                next(f)
                content_lines = f.readlines()
            for row in content_lines:
                row = row.split(',')
                side_effect = SideEffect()
                medication = Medication()
                medication.medication_name = row[0].strip()
                side_effect.side_effect = row[1].strip()
                side_effect.date_published = row[2].strip()
                #print(row[0].strip())
                #side_effect.save()
            print(medication.medication_name)

        else:
            print('Error: specify file')
from django.core.management.base import BaseCommand
from drugs.models import Medication, SideEffect


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument(
            '--side_effects_data_file',
            action='store_true',
            help='Name of the file with medication side effects data'
        )


    def handle(self, *args, **options):
        # get the name of the file to import from arguments
        side_effect_data_filename = options['side_effects_data_file']
        #if options['medication_data_file']:


        # if filename is not empty, open the file and read all lines
        if side_effect_data_filename:
            content_lines = []


            with open('medication_side_effects_database.txt', 'r') as f:
                content_lines = f.read().split(',')
                for row in content_lines:
                    #content_lines.append(row.split(','))
                    row = row.split(',')
                    side_effect = SideEffect()
                    side_effect.side_effect = row[0]
                    #side_effect.date_published = row[]
                    #side_effect.save()
                    print(side_effect.side_effect)

        else:
            print('Error: specify file')
from django.core.management.base import BaseCommand
from drugs.models import Medication, SideEffect


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument(
            '--side_effects_data_file',
            help='Name of the file with medication side effects data'
        )


    def handle(self, *args, **options):
        # get the name to import from arguments
        side_effect_data_filename = options['side_effects_data_file']

        # check if file is not empty
        if side_effect_data_filename:
            content_lines = []
            # open file for reading
            with open(side_effect_data_filename, 'r') as f:
                # skip first line
                next(f)
                # reading all lines
                content_lines = f.readlines()


            # loop through all rows
            for row in content_lines:
                # split the rows
                row = row.split(',')
                # get the medication name
                medicationName = row[0].strip()
                # filter
                med = Medication.objects.filter(medication_name=medicationName).first()
                # if medication is not exist in database print error, if exist continue
                if not med:
                    print('error: can not find medication %s associated with side effect' % medicationName)
                    continue
                # create SideEffect object
                sideEffect = SideEffect()
                # add all fields
                sideEffect.medication = med
                sideEffect.side_effect = row[1].strip()
                sideEffect.date_published = row[2].strip()
                # save sideEffect to database
                sideEffect.save()
                print(sideEffect.date_published)

        else:
            print('Error: specify file')
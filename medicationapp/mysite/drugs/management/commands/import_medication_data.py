from django.core.management.base import BaseCommand
from drugs.models import Medication


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument(
            '--medication_data_file',
            help='Name of the file with medication data'
        )


    def handle(self, *args, **options):
        # get the name of the file to import from arguments
        medication_data_filename = options['medication_data_file']

        print(medication_data_filename)

        # check if filename was specified
        if medication_data_filename:
            content_lines = []

            # open the file for reading
            with open(medication_data_filename, 'r') as f:
                # skip one row (header row)
                next(f)

                # read all lines from file
                content_lines = f.readlines()

            # go through each row
            for row in content_lines:
                # split row into tokens
                row = row.split(',')
                # create empty Medication object
                medication = Medication()
                # add fields
                medication.medication_name = row[0].strip()
                medication.manufacturer = row[1].strip()
                medication.date_on_market = row[2].strip()
                medication.status = row[3].strip()

                # look up all records in database with the same: name
                db_records = Medication.objects.filter(medication_name=medication.medication_name).count()

                # if records exist in database with same name and date_on_market, print error and continue to next line
                if db_records > 0:
                    print('error: medication already exists %s' % medication.medication_name)
                    continue
                else:
                    # save new medication to database
                    medication.save()
                    print('saved new medication %s' % medication.medication_name)
        else:
            print('Error: specify file')

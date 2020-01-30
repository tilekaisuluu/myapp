from django.core.management.base import BaseCommand
from drugs.models import Medication


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument(
            '--medication_data_file',
            action='store_true',
            help='Name of the file with medication data'
        )


    def handle(self, *args, **options):
        # get the name of the file to import from arguments
        medication_data_filename = options['medication_data_file']
        #if options['medication_data_file']:


        # if filename is not empty, open the file and read all lines
        if medication_data_filename:
            content_lines = []

            with open('medication_database.txt', 'r') as f:
                content_lines = f.read().split(',')
                for row in content_lines:
                    #content_lines.append(row.split(','))
                    row = row.split(',')
                    medication = Medication()
                    medication.medication_name = row[0]
                   #medication.manufacturer = row[1]
                   #medication.date_on_market = row[]
                   #medication.status = row[]
                    #medication.save()
                    print(medication)

            # for each line in the content lines
            #   separate the line into tokens (split the line)
            #   build Medication object (use token index)
            #       check if medication with same name already exists?
            #   print log message (ex: print(m.mediaction_name))
            #   save Medication object (persist)

        else:
            print('Error: specify file')

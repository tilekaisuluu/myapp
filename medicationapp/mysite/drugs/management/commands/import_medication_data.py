from django.core.management.base import BaseCommand
from drugs.models import Medication as Drug


class Command(BaseCommand):

    def handle(self, *args, **options):
        # get the name of the file to import from arguments
        medication_data_filename = options['medication_data_file']

        # if filename is not empty, open the file and read all lines
        if medication_data_filename:
            content_lines = []

            # open file and read all lines
            with open(medication_data_filename) as f:
                content_lines = f.readlines()

            # for each line in the content lines
            #   separate the line into tokens (split the line)
            #   build Medication object (use token index)
            #       check if medication with same name already exists?
            #   print log message (ex: print(m.mediaction_name))
            #   save Medication object (persist)

        else:
            print('Error: specify file')



    def add_arguments(self, parser):
        parser.add_argument(
            '--medication_data_file',
            help='Name of the file with medication data'
        )
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
                #print(row)
                medication = Medication()
                medication.medication_name = row[0].strip()
                medication.manufacturer = row[1].strip()
                #print(row[2].strip())

                medication.date_on_market = row[2].strip()
                medication.status = row[3].strip()
                duplicates = Medication.objects.values(
                    'medication_name'
                ).annotate(name_count=Count('medication_name')).filter(name_count__gt=1)
                records = Medication.objects.filter(first_name__in=[item['medication_name'] for item in duplicates])
                print([item.id for item in records])



                #for medication in with_duplicates:
                    #duplicates = Medication.objects.filter(name=medication.medication_name).exclude(id=medication.id)
                #medication.save()
                #print(medication.manufacturer)


        else:
            print('Error: specify file')

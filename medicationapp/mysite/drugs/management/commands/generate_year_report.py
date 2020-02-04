from django.core.management.base import BaseCommand
from drugs.models import Medication, SideEffect

class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument(
            '--year',
            type=str,
            help='Year for which to generate the report'
        )

    def handle(self, *args, **options):

        #
        # BUG: check if "year" argument is set, if not: return error
        #


        # find all medication with date_on_market year same as year specified in CLI (look at https://docs.djangoproject.com/en/3.0/intro/tutorial02/)
        year = options['year']
        medication_list = Medication.objects.filter(date_on_market__year=year) #.values_list('medication_name', 'manufacturer', 'date_on_market')

        for med in medication_list:
            print("%s :: %s :: %s" % (med.medication_name, med.manufacturer, med.date_on_market))


        # ....
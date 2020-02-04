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
        # get the year to import from arguments
        year = options["year"]

        # check if year specified
        if options["year"]:
            # filter all medication with date_on_market year same as year specified in CLI
            medication_list = Medication.objects.filter(date_on_market__year=year)
            # loop through the list to print medication name :: manufacturer :: date_on_market
            for med in medication_list:
                print("%s :: %s :: %s" % (med.medication_name, med.manufacturer, med.date_on_market))
            # filter all side_effects with date published year same as year specified in ClI
            side_effect_list = SideEffect.objects.filter(date_published__year=year)
            # loop through the list to print side effect -> medication name
            for side_effect in side_effect_list:
                print("%s -> %s" % (side_effect.side_effect, side_effect.medication))


        else:
            print('Error: specify year')
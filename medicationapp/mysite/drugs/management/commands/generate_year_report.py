from django.core.management.base import BaseCommand
from drugs.models import Medication, SideEffect


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument(
            '--year',
            type=int,
            help='Year for which to generate the report'
        )

    def handle(self, *args, **options):

        # find all medication with date_on_market year same as year specified in CLI (look at https://docs.djangoproject.com/en/3.0/intro/tutorial02/)

        # print them all with columns: (google search: "python string interpolation tutorial")
            # name :: manufacturer :: date_on_market
            # xyz :: Another Drug Company :: 2000-02-01

        # find all sideeffects with date_published year same as year specified in CLI

        # print them all with columns:
            # side_effect -> drug_name
            # headache -> aspirin

        pass
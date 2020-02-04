from django.db import models


class Medication(models.Model):
    medication_name = models.CharField(max_length=200)
    manufacturer = models.CharField(max_length=200)
    date_on_market = models.DateField(blank=True, null=True)
    status = models.IntegerField(null = True, blank = True)

    def __str__(self):
        return self.medication_name

class SideEffect(models.Model):
    medication = models.ForeignKey(Medication, on_delete=models.CASCADE, null=True, blank = True)
    side_effect = models.CharField(max_length=200)
    date_published = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.side_effect





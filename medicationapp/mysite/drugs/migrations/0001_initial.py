# Generated by Django 3.0.2 on 2020-01-23 10:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Medication',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('medication_name', models.CharField(max_length=200)),
                ('manufacturer', models.CharField(max_length=200)),
                ('date_on_market', models.DateField()),
                ('status', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='SideEffect',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('side_effect', models.CharField(max_length=200)),
                ('date_published', models.DateField()),
                ('medication', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='drugs.Medication')),
            ],
        ),
    ]

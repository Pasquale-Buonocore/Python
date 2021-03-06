# Generated by Django 2.0.3 on 2018-03-30 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProcessData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_stamp', models.DateTimeField()),
                ('Pulsometer_readout', models.DecimalField(decimal_places=14, max_digits=16)),
                ('Engine_efficiency', models.IntegerField()),
                ('red_Value', models.IntegerField()),
                ('blue_Value', models.IntegerField()),
                ('green_Value', models.IntegerField()),
            ],
        ),
    ]

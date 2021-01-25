# Generated by Django 2.2 on 2020-10-06 14:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('assays', '0026_hpibd02'),
    ]

    operations = [
        migrations.CreateModel(
            name='Iinflc03',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timepoint', models.IntegerField(blank=True, null=True)),
                ('age', models.IntegerField(blank=True, null=True)),
                ('measurement_date', models.DateField(blank=True, null=True)),
                ('sum_intensity', models.FloatField(blank=True, null=True)),
                ('net_intensity', models.FloatField(blank=True, null=True)),
                ('mean_intensity', models.FloatField(blank=True, null=True)),
                ('acquisition_settings', models.TextField(blank=True, null=True)),
                ('comment', models.TextField(blank=True, null=True)),
                ('assayid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='iinflc03s', to='assays.Assay')),
                ('mid', models.ForeignKey(db_column='mid', on_delete=django.db.models.deletion.CASCADE, to='assays.Mouse')),
            ],
            options={
                'managed': True,
                'db_table': 'IINFLC-03',
            },
        ),
    ]
# Generated by Django 2.2 on 2021-02-18 11:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('assays', '0002_hpni01'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fc08',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timepoint', models.IntegerField(blank=True, null=True)),
                ('age', models.IntegerField(blank=True, null=True)),
                ('measurement_date', models.DateField(blank=True, null=True)),
                ('sample_source', models.CharField(blank=True, max_length=64, null=True)),
                ('facs_lysing', models.CharField(blank=True, max_length=32, null=True)),
                ('live_aquis', models.CharField(blank=True, max_length=16, null=True)),
                ('total_cell_count', models.FloatField(blank=True, null=True)),
                ('neu_per', models.FloatField(blank=True, null=True)),
                ('eos_per', models.FloatField(blank=True, null=True)),
                ('mon_per', models.FloatField(blank=True, null=True)),
                ('ly6chimono_per', models.FloatField(blank=True, null=True)),
                ('ly6cintermono_per', models.FloatField(blank=True, null=True)),
                ('ly6clowmono_per', models.FloatField(blank=True, null=True)),
                ('dcs_per', models.FloatField(blank=True, null=True)),
                ('nk_cells_per', models.FloatField(blank=True, null=True)),
                ('b_cells_per', models.FloatField(blank=True, null=True)),
                ('t_cells_per', models.FloatField(blank=True, null=True)),
                ('neu_num', models.FloatField(blank=True, null=True)),
                ('eos_num', models.FloatField(blank=True, null=True)),
                ('mon_num', models.FloatField(blank=True, null=True)),
                ('ly6chimono_num', models.FloatField(blank=True, null=True)),
                ('ly6cintermono_num', models.FloatField(blank=True, null=True)),
                ('ly6clowmono_num', models.FloatField(blank=True, null=True)),
                ('dcs_num', models.FloatField(blank=True, null=True)),
                ('nk_cells_num', models.FloatField(blank=True, null=True)),
                ('b_cells_num', models.FloatField(blank=True, null=True)),
                ('t_cells_num', models.FloatField(blank=True, null=True)),
                ('total_cell_count_2', models.FloatField(blank=True, null=True)),
                ('b_cells_per_2', models.FloatField(blank=True, null=True)),
                ('nk_cells_per_2', models.FloatField(blank=True, null=True)),
                ('cd4_per', models.FloatField(blank=True, null=True)),
                ('cd4_cd25_per', models.FloatField(blank=True, null=True)),
                ('comment', models.TextField(blank=True, null=True)),
                ('assayid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fc08s', to='assays.Assay')),
                ('mid', models.ForeignKey(db_column='mid', on_delete=django.db.models.deletion.CASCADE, to='assays.Mouse')),
            ],
            options={
                'db_table': 'FC-08',
                'managed': True,
            },
        ),
    ]

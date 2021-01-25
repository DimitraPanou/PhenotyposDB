# Generated by Django 2.2 on 2020-10-05 09:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('assays', '0019_ni02ofd01'),
    ]

    operations = [
        migrations.AddField(
            model_name='ni02ofd01',
            name='comment',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='ni02rot01',
            name='comment',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.CreateModel(
            name='Ni02grs01',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timepoint', models.IntegerField(blank=True, null=True)),
                ('age', models.IntegerField(blank=True, null=True)),
                ('measurement_date', models.DateField(blank=True, null=True)),
                ('forelimb_r1', models.FloatField(blank=True, null=True)),
                ('forelimb_r2', models.FloatField(blank=True, null=True)),
                ('forelimb_r3', models.FloatField(blank=True, null=True)),
                ('hindlimb_r1', models.FloatField(blank=True, null=True)),
                ('hindlimb_r2', models.FloatField(blank=True, null=True)),
                ('hindlimb_r3', models.FloatField(blank=True, null=True)),
                ('forelimb', models.FloatField(blank=True, null=True)),
                ('hindlimb', models.FloatField(blank=True, null=True)),
                ('weight', models.FloatField(blank=True, null=True)),
                ('forelimb_mean_ratio', models.FloatField(blank=True, null=True)),
                ('hindlimb_mean_ratio', models.FloatField(blank=True, null=True)),
                ('comment', models.TextField(blank=True, null=True)),
                ('assayid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ni02grs01s', to='assays.Assay')),
                ('mid', models.ForeignKey(db_column='mid', on_delete=django.db.models.deletion.CASCADE, to='assays.Mouse')),
            ],
            options={
                'db_table': 'NI-02-GRS-01',
                'managed': True,
            },
        ),
    ]
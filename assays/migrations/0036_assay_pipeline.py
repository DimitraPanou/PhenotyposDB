# Generated by Django 2.2 on 2020-10-08 20:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pipelines', '0002_auto_20201008_1456'),
        ('assays', '0035_auto_20201006_1821'),
    ]

    operations = [
        migrations.AddField(
            model_name='assay',
            name='pipeline',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='assays', to='pipelines.Pipeline'),
        ),
    ]
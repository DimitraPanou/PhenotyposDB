# Generated by Django 2.2 on 2021-06-17 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assays', '0022_fc03'),
    ]

    operations = [
        migrations.AddField(
            model_name='fc04',
            name='sample_id',
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
    ]

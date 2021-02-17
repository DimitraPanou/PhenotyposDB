# Generated by Django 2.2 on 2021-02-01 11:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='PipelineType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.TextField()),
                ('name', models.CharField(blank=True, max_length=256, null=True)),
            ],
            options={
                'db_table': 'pipelinetypes',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Pipeline',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=128, null=True)),
                ('model', models.CharField(blank=True, max_length=32, null=True)),
                ('protocol', models.TextField(blank=True, null=True)),
                ('pip_start', models.DateField(blank=True, null=True)),
                ('pip_end', models.DateField(blank=True, null=True)),
                ('status', models.CharField(blank=True, max_length=32, null=True)),
                ('pipelineqc', models.CharField(blank=True, db_column='pipelineQC', max_length=256, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('pi', models.ForeignKey(db_column='pi', default=1, on_delete=django.db.models.deletion.DO_NOTHING, related_name='pipelines', to=settings.AUTH_USER_MODEL)),
                ('type', models.ForeignKey(db_column='type', on_delete=django.db.models.deletion.DO_NOTHING, to='pipelines.PipelineType')),
            ],
            options={
                'db_table': 'pipelines',
                'managed': True,
            },
        ),
    ]

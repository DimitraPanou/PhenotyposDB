from django.db import models

from django.contrib.auth.models import User

# Create your models here.

class PipelineType(models.Model):
    code = models.TextField()  # This field type is a guess.
    name = models.CharField(max_length=256, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'pipelinetypes'

    def __str__(self):
        return u'{0}'.format(self.code)

    def get_edit_url(self):
        return reverse('pipelinetype-update', kwargs={'pk': self.id})


class Pipeline(models.Model):
    STATUS = (
        ('Pending', 'Pending'),
        ('Done', 'Done'),
    )
    name = models.CharField(max_length=128, blank=True, null=True)
    model = models.CharField(max_length=32, blank=True, null=True)
    protocol = models.TextField(blank=True, null=True)  # This field type is a guess.
    pip_start = models.DateField(blank=True, null=True)
    pip_end = models.DateField(blank=True, null=True)
    status = models.CharField(
        max_length=32,
        choices=STATUS,
        default='Pending',
    )
    pipelineqc = models.CharField(db_column='pipelineQC', max_length=256, blank=True, null=True)  # Field name made lowercase.
    pi = models.ForeignKey(User, on_delete=models.DO_NOTHING,db_column='pi',default=1, related_name='pipelines')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    type = models.ForeignKey(PipelineType, models.DO_NOTHING, db_column='type')

    class Meta:
        managed = True
        db_table = 'pipelines'

    def get_absolute_url(self):
        return reverse('pipeline-detail', kwargs={'pk': self.pk})

    def __str__(self):
        return u'{0}\t\t{1}'.format(self.name, self.model)

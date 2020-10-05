from django.db import models
from django.contrib.auth.models import User
# Create your models here.

#Atype
class Atype(models.Model):
    code = models.CharField(max_length=16)
    name = models.CharField(max_length=256, blank=True, null=True)
    facility = models.CharField(max_length=16, blank=True, null=True)
    unit = models.CharField(max_length=32, blank=True, null=True)
    staff = models.CharField(max_length=256, blank=True, null=True)
    publication_date = models.DateField(blank=True, null=True)
    version = models.IntegerField(blank=True, null=True)
    assay_word = models.FileField(blank=True,upload_to='assays/types/{0}/'.format(code))
    purpose = models.TextField(blank=True, null=True)
    experimental_design = models.TextField(blank=True, null=True)
    equipment = models.TextField(blank=True, null=True)
    supplies = models.TextField(blank=True, null=True)
    procedures = models.TextField(blank=True, null=True)
    troubleshooting = models.TextField(blank=True, null=True)
    appendix = models.TextField(blank=True, null=True)
    references = models.TextField(blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return u'{0}'.format(self.code)

    #def get_absolute_url(self):
    #    return reverse('assaytype-detail', kwargs={'pk': self.id})

    def get_edit_url(self):
        return reverse('assaytype-detail-update', kwargs={'pk': self.id})

class Assay(models.Model):
    code = models.CharField(max_length=25)
    name = models.CharField(max_length=128, blank=True, null=True)
    version = models.IntegerField(blank=True, null=True)
    staff = models.CharField(max_length=128, blank=True, null=True)
    comments = models.TextField(blank=True, null=True)
    measurement_day = models.DateField(blank=True, null=True)
    rawdata_file = models.FileField(upload_to='assays/xlsx/')
    assayqc = models.CharField(db_column='assayQC', max_length=256, blank=True, null=True)  # Field name made lowercase.
    type = models.ForeignKey('Atype', models.DO_NOTHING, db_column='type')
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING,db_column='author',default=1, related_name='created_by_user')
    updated_by = models.ForeignKey(User,on_delete=models.DO_NOTHING, related_name='updated_by_user',blank=True, null=True)
    #scientist = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name="scientists",related_query_name="scientist",)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def get_absolute_url(self):
        return reverse('assay-detail', kwargs={'pk': self.pk})

    def __str__(self):
        return u'{0}\t\t{1}'.format(self.name, self.code)

class Iinflc04(models.Model):
    assayid = models.ForeignKey('Assay', on_delete=models.CASCADE,related_name='iinflc04s')  # Field name made lowercase.
    mid = models.ForeignKey('Mouse', on_delete=models.CASCADE, db_column='mid')
    timepoint = models.IntegerField(blank=True, null=True)
    #timepoint_type = models.CharField(max_length=16)
    age = models.IntegerField(blank=True, null=True)
    measurement_date = models.DateField(blank=True, null=True)
    weight = models.FloatField(blank=True, null=True)
    comment = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'IINFLC-04'

class Ni01(models.Model):
    assayid = models.ForeignKey('Assay', on_delete=models.CASCADE, related_name='ni01s')  # Field name made lowercase.
    mid = models.ForeignKey('Mouse', on_delete=models.CASCADE, db_column='mid')
    timepoint = models.IntegerField(blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    measurement_date = models.DateField(blank=True, null=True)
    clinical_score = models.FloatField(blank=True, null=True)
    comment = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'NI-01'

class Ni02Rot01(models.Model):
    assayid = models.ForeignKey('Assay', on_delete=models.CASCADE,related_name='ni02rot01s')  # Field name made lowercase.
    mid = models.ForeignKey('Mouse', on_delete=models.CASCADE, db_column='mid')
    timepoint = models.IntegerField(blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    measurement_date = models.DateField(blank=True, null=True)
    individual_latency_fall1 = models.FloatField(blank=True, null=True)
    individual_latency_fall2 = models.FloatField(blank=True, null=True)
    mean_latency_fall = models.FloatField(blank=True, null=True)
    speed_fall1 = models.FloatField(blank=True, null=True)
    speed_fall2 = models.FloatField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'NI-02-ROT-01'

class Ni02ofd01(models.Model):
    assayid = models.ForeignKey('Assay', on_delete=models.CASCADE,related_name='ni02ofd01s')  # Field name made lowercase.
    mid = models.ForeignKey('Mouse', on_delete=models.CASCADE, db_column='mid')
    timepoint = models.IntegerField(blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    measurement_date = models.DateField(blank=True, null=True)
    total_distance_wa = models.FloatField(blank=True, null=True)
    total_distance_cz = models.FloatField(blank=True, null=True)
    total_distance_pz = models.FloatField(blank=True, null=True)
    total_rears = models.FloatField(blank=True, null=True)
    rears_cz = models.FloatField(blank=True, null=True)
    rears_pz = models.FloatField(blank=True, null=True)
    time_cz = models.FloatField(blank=True, null=True)
    time_pz = models.FloatField(blank=True, null=True)
    duration_immobility_wa = models.FloatField(blank=True, null=True)
    duration_immobility_cz = models.FloatField(blank=True, null=True)
    duration_immobility_pz = models.FloatField(blank=True, null=True)
    avg_speed_wa = models.FloatField(blank=True, null=True)
    avg_speed_cz = models.FloatField(blank=True, null=True)
    avg_speed_pz = models.FloatField(blank=True, null=True)
    num_entries_cz = models.FloatField(blank=True, null=True)
    latency1_cz = models.FloatField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'NI-02-OFD-01'

class Mouse(models.Model):
    GENDER = (
        ('Male', 'Male'),
        ('Female', 'Female'),
    )
    GENOTYPE = (
        ('WT', 'Wildtype'),
        ('TG', 'Transgenic'),
    )
    mid = models.CharField(max_length=128, blank=False, null=False, unique=True)
    strain = models.CharField(max_length=128, blank=True, null=True)
    tail_num = models.IntegerField(blank=True, null=True)    
    genotype = models.CharField(max_length=128, blank=True, null=True)
    induced = models.CharField(max_length=32, blank=True, null=True)
    treated = models.CharField(max_length=32, blank=True, null=True)
    gender = models.CharField(max_length=16, blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    dateofBirth = models.DateField(blank=True, null=True)
    diet = models.TextField(blank=True, null=True)
    mouse_info = models.TextField(blank=True, null=True)
    other = models.TextField(blank=True, null=True)
    #health_report = models.CharField(max_length=256, blank=True, null=True)

    def __str__(self):
        return u'{0}'.format(self.mid)
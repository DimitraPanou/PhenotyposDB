from django.db import models
from django.contrib.auth.models import User

from pipelines.models import Pipeline
# Create your models here.
from ckeditor.fields import RichTextField

class Facility(models.Model):
    name = models.CharField(max_length=256, blank=True, null=True)
    details = models.TextField(blank=True, null=True)
    def __str__(self):
        return u'{0}'.format(self.name)
#Atype
class Atype(models.Model):
    code = models.CharField(max_length=16)
    name = models.CharField(max_length=256, blank=True, null=True)
    facility = models.CharField(max_length=16, blank=True, null=True)
    facilitylong = models.ForeignKey('Facility', models.DO_NOTHING, db_column ="facilitylong")
    unit = models.CharField(max_length=32, blank=True, null=True)
    staff = models.CharField(max_length=256, blank=True, null=True)
    publication_date = models.DateField(blank=True, null=True)
    version = models.IntegerField(blank=True, null=True)
    assay_word = models.FileField(blank=True,upload_to='assays/types/{0}/'.format(code))
    purpose = RichTextField(blank=True, null=True)
    experimental_design = RichTextField(blank=True, null=True)
    equipment = RichTextField(blank=True, null=True)
    supplies = RichTextField(blank=True, null=True)
    procedures = RichTextField(blank=True, null=True)
    troubleshooting = RichTextField(blank=True, null=True)
    appendix = RichTextField(blank=True, null=True)
    references = RichTextField(blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return u'{0} ({1})'.format(self.code, self.facilitylong.name)

    #def get_absolute_url(self):
    #    return reverse('assaytype-detail', kwargs={'pk': self.id})

    def get_edit_url(self):
        return reverse('assaytype-detail-update', kwargs={'pk': self.id})

class Assay(models.Model):
    MOUSEAGE = (
        ('days', 'days'),
        ('weeks', 'weeks'),
    )
    TIMESTEPS = (
        ('hours', 'hours'),        
        ('days', 'days'),
        ('weeks', 'weeks'),
    )    
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
    pipeline = models.ForeignKey(Pipeline, on_delete=models.DO_NOTHING, related_name='assays',blank=True, null=True)
    updated_by = models.ForeignKey(User,on_delete=models.DO_NOTHING, related_name='updated_by_user',blank=True, null=True)
    scientist = models.ForeignKey(User, on_delete=models.DO_NOTHING,db_column='scientist', related_name='scientists',related_query_name='scientist',blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    mouse_age = models.CharField(
        max_length=7,
        choices=MOUSEAGE,
        default='days',
    )
    duration = models.IntegerField(blank=True, null=True)    
    timesteps_in = models.CharField(
        max_length=7,
        choices=TIMESTEPS,
        default='days',
    )



    def get_absolute_url(self):
        return reverse('assay-detail', kwargs={'pk': self.pk})

    def __str__(self):
        return u'{0}\t\t{1}'.format(self.name, self.code)

class AssociatedImage(models.Model):
    assayid = models.ForeignKey('Assay', on_delete=models.CASCADE, related_name='associated_images')  # Field name made lowercase.
    title = models.CharField(max_length=50, blank=True, null=True)
    image = models.ImageField(upload_to='assays/img/')
    caption = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'AssociatedImages'

    def __str__(self):
        return u'{0}'.format(self.title)

class Iinflc01(models.Model):
    assayid = models.ForeignKey('Assay', on_delete=models.CASCADE, related_name='iinflc01s')  # Field name made lowercase.
    mid = models.ForeignKey('Mouse', on_delete=models.CASCADE, db_column='mid')
    timepoint = models.IntegerField(blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    measurement_date = models.DateField(blank=True, null=True)
    weight = models.FloatField(blank=True, null=True)
    stool_consistency = models.FloatField(blank=True, null=True)
    blood_in_stool = models.FloatField(blank=True, null=True)
    weight_score = models.FloatField(blank=True, null=True)
    dai = models.CharField(max_length=128, blank=True, null=True)
    comments = models.CharField(max_length=256, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'IINFLC-01'

class Iinflc02(models.Model):
    assayid = models.ForeignKey('Assay', on_delete=models.CASCADE, related_name='iinflc02s')  # Field name made lowercase.
    mid = models.ForeignKey('Mouse', on_delete=models.CASCADE, db_column='mid')
    timepoint = models.IntegerField(blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    measurement_date = models.DateField(blank=True, null=True)
    sample_source = models.CharField(max_length=256, blank=True, null=True)
    cell_count_s_intestine = models.FloatField(blank=True, null=True)
    cell_count_l_intestine = models.FloatField(blank=True, null=True)
    comment = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'IINFLC-02'

class Iinflc03(models.Model):
    assayid = models.ForeignKey('Assay', on_delete=models.CASCADE, related_name='iinflc03s')  # Field name made lowercase.
    mid = models.ForeignKey('Mouse', on_delete=models.CASCADE, db_column='mid')
    timepoint = models.IntegerField(blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    measurement_date = models.DateField(blank=True, null=True)
    sum_intensity = models.FloatField(blank=True, null=True)
    net_intensity = models.FloatField(blank=True, null=True)
    mean_intensity = models.FloatField(blank=True, null=True)
    acquisition_settings = models.TextField(blank=True, null=True)
    comment = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'IINFLC-03'

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

class Iinflc05(models.Model):
    assayid = models.ForeignKey('Assay', on_delete=models.CASCADE, related_name='iinflc05s')  # Field name made lowercase.
    mid = models.ForeignKey('Mouse', on_delete=models.CASCADE, db_column='mid')
    timepoint = models.IntegerField(blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    measurement_date = models.DateField(blank=True, null=True)
    sum_intensity = models.FloatField(blank=True, null=True)
    net_intensity = models.FloatField(blank=True, null=True)
    mean_intensity = models.FloatField(blank=True, null=True)
    acquisition_settings = models.TextField(blank=True, null=True)
    comment = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'IINFLC-05'

class Iinflc06(models.Model):
    assayid = models.ForeignKey('Assay', on_delete=models.CASCADE, related_name='iinflc06s')  # Field name made lowercase.
    mid = models.ForeignKey('Mouse', on_delete=models.CASCADE, db_column='mid')
    timepoint = models.IntegerField(blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    measurement_date = models.DateField(blank=True, null=True)
    sum_intensity = models.FloatField(blank=True, null=True)
    net_intensity = models.FloatField(blank=True, null=True)
    mean_intensity = models.FloatField(blank=True, null=True)
    acquisition_settings = models.TextField(blank=True, null=True)
    comment = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'IINFLC-06'

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
    comment = models.TextField(blank=True, null=True)

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
    comment = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'NI-02-OFD-01'

class Ni02grs01(models.Model):
    assayid = models.ForeignKey('Assay', on_delete=models.CASCADE,related_name='ni02grs01s')  # Field name made lowercase.
    mid = models.ForeignKey('Mouse', on_delete=models.CASCADE, db_column='mid')
    timepoint = models.IntegerField(blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    measurement_date = models.DateField(blank=True, null=True)
    forelimb_r1 = models.FloatField(blank=True, null=True)
    forelimb_r2 = models.FloatField(blank=True, null=True)
    forelimb_r3 = models.FloatField(blank=True, null=True)
    hindlimb_r1 = models.FloatField(blank=True, null=True)
    hindlimb_r2 = models.FloatField(blank=True, null=True)
    hindlimb_r3 = models.FloatField(blank=True, null=True)
    forelimb = models.FloatField(blank=True, null=True)
    hindlimb = models.FloatField(blank=True, null=True)
    weight = models.FloatField(blank=True, null=True)
    forelimb_mean_ratio = models.FloatField(blank=True, null=True)
    hindlimb_mean_ratio = models.FloatField(blank=True, null=True)
    comment = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'NI-02-GRS-01'

class Hem01(models.Model):
    assayid = models.ForeignKey('Assay', on_delete=models.CASCADE,related_name='hem01s')  # Field name made lowercase.
    mid = models.ForeignKey('Mouse', on_delete=models.CASCADE, db_column='mid')
    timepoint = models.IntegerField(blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    measurement_date = models.DateField(blank=True, null=True)
    sample_id = models.CharField(max_length=128, blank=True, null=True)
    wbc_count = models.FloatField(blank=True, null=True)
    mononuclear_num = models.FloatField(blank=True, null=True)
    lymphocytes_num = models.FloatField(blank=True, null=True)
    lymphocytes_per = models.FloatField(blank=True, null=True)
    monocytes_num = models.FloatField(blank=True, null=True)
    monocytes2_num = models.FloatField(blank=True, null=True)
    neutrophils_num = models.FloatField(blank=True, null=True)
    neutrophils_per = models.FloatField(blank=True, null=True)
    eosinophils_num = models.FloatField(blank=True, null=True)
    eosinophils_per = models.FloatField(blank=True, null=True)
    basophils_num = models.FloatField(blank=True, null=True)
    basophils_per = models.FloatField(blank=True, null=True)
    rbc_count = models.FloatField(blank=True, null=True)
    ht = models.FloatField(blank=True, null=True)
    hb = models.FloatField(blank=True, null=True)
    plt_count = models.FloatField(blank=True, null=True)
    platelet_dist_range = models.FloatField(blank=True, null=True)
    platelet_count = models.FloatField(blank=True, null=True)
    avg_vol_platelets = models.FloatField(blank=True, null=True)
    mcv = models.FloatField(blank=True, null=True)
    rdv = models.FloatField(blank=True, null=True)
    mchc = models.FloatField(blank=True, null=True)
    mcv2 = models.FloatField(blank=True, null=True)
    comment = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'HEM-01'

class Hpibd02(models.Model):
    assayid = models.ForeignKey('Assay', on_delete=models.CASCADE,related_name='hpibd02s')  # Field name made lowercase.
    mid = models.ForeignKey('Mouse', on_delete=models.CASCADE, db_column='mid')
    timepoint = models.IntegerField(blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    measurement_date = models.DateField(blank=True, null=True)
    inflammation_small = models.FloatField(blank=True, null=True)
    epithelial_small = models.FloatField(blank=True, null=True)
    inflammation_large = models.FloatField(blank=True, null=True)
    epithelial_large = models.FloatField(blank=True, null=True)
    vc_ratio = models.FloatField(blank=True, null=True)
    colon_length = models.FloatField(blank=True, null=True)
    epithelium_s_flattening = models.FloatField(blank=True, null=True)
    apoptotic_s_field = models.FloatField(blank=True, null=True)
    goblet_s_depletion = models.FloatField(blank=True, null=True)
    lumen_s_exfoliation = models.FloatField(blank=True, null=True)
    villus_s_short = models.FloatField(blank=True, null=True)
    igd_small = models.FloatField(blank=True, null=True)
    paneth_s_activation = models.FloatField(blank=True, null=True)
    peyer_s_patch = models.FloatField(blank=True, null=True)
    apoptotic_l_field = models.FloatField(blank=True, null=True)
    goblet_l_depletion = models.FloatField(blank=True, null=True)
    lumen_l_exfoliation = models.FloatField(blank=True, null=True)
    crypt_l_damage = models.FloatField(blank=True, null=True)
    endothelial_l_activation = models.FloatField(blank=True, null=True)
    comment = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'HPIBD-02'


class Biochem01(models.Model):
    assayid = models.ForeignKey('Assay', on_delete=models.CASCADE,related_name='biochem01s')  # Field name made lowercase.
    mid = models.ForeignKey('Mouse', on_delete=models.CASCADE, db_column='mid')
    timepoint = models.IntegerField(blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    measurement_date = models.DateField(blank=True, null=True)
    sample_source = models.CharField(max_length=64, blank=True, null=True)
    total_protein = models.FloatField(blank=True, null=True)
    albumin = models.FloatField(blank=True, null=True)
    comment = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'BIOCHEM-01'

class Biochem02(models.Model):
    assayid = models.ForeignKey('Assay', on_delete=models.CASCADE,related_name='biochem02s')  # Field name made lowercase.
    mid = models.ForeignKey('Mouse', on_delete=models.CASCADE, db_column='mid')
    timepoint = models.IntegerField(blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    measurement_date = models.DateField(blank=True, null=True)
    sodium = models.FloatField(blank=True, null=True)
    potassium = models.FloatField(blank=True, null=True)
    chloride = models.FloatField(blank=True, null=True)
    phosphorus = models.FloatField(blank=True, null=True)
    calcium = models.FloatField(blank=True, null=True)
    magnesium = models.FloatField(blank=True, null=True)
    comment = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'BIOCHEM-02'

class Biochem03(models.Model):
    assayid = models.ForeignKey('Assay', on_delete=models.CASCADE,related_name='biochem03s')  # Field name made lowercase.
    mid = models.ForeignKey('Mouse', on_delete=models.CASCADE, db_column='mid')
    timepoint = models.IntegerField(blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    measurement_date = models.DateField(blank=True, null=True)
    sample_source = models.CharField(max_length=64, blank=True, null=True)
    alt = models.FloatField(blank=True, null=True)
    ast = models.FloatField(blank=True, null=True)
    alp = models.FloatField(blank=True, null=True)
    total_bilirubin = models.FloatField(blank=True, null=True)
    direct_bilirubin = models.FloatField(blank=True, null=True)
    comment = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'BIOCHEM-03'

class Biochem04(models.Model):
    assayid = models.ForeignKey('Assay', on_delete=models.CASCADE,related_name='biochem04s')  # Field name made lowercase.
    mid = models.ForeignKey('Mouse', on_delete=models.CASCADE, db_column='mid')
    timepoint = models.IntegerField(blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    measurement_date = models.DateField(blank=True, null=True)
    sample_source = models.CharField(max_length=64, blank=True, null=True)
    urea = models.FloatField(blank=True, null=True)
    uric_acid = models.FloatField(blank=True, null=True)
    creatinine = models.FloatField(blank=True, null=True)
    comment = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'BIOCHEM-04'

class Biochem05(models.Model):
    assayid = models.ForeignKey('Assay', on_delete=models.CASCADE,related_name='biochem05s')  # Field name made lowercase.
    mid = models.ForeignKey('Mouse', on_delete=models.CASCADE, db_column='mid')
    timepoint = models.IntegerField(blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    measurement_date = models.DateField(blank=True, null=True)
    sample_source = models.CharField(max_length=64, blank=True, null=True)
    amylase = models.FloatField(blank=True, null=True)
    lipase = models.FloatField(blank=True, null=True)
    glucose = models.FloatField(blank=True, null=True)
    comment = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'BIOCHEM-05'

class Biochem06(models.Model):
    assayid = models.ForeignKey('Assay', on_delete=models.CASCADE,related_name='biochem06s')  # Field name made lowercase.
    mid = models.ForeignKey('Mouse', on_delete=models.CASCADE, db_column='mid')
    timepoint = models.IntegerField(blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    measurement_date = models.DateField(blank=True, null=True)
    sample_source = models.CharField(max_length=64, blank=True, null=True)
    cholesterol = models.FloatField(blank=True, null=True)
    hdl_cholesterol = models.FloatField(blank=True, null=True)
    ldl_cholesterol = models.FloatField(blank=True, null=True)
    triglycerides = models.FloatField(blank=True, null=True)
    nefa = models.FloatField(blank=True, null=True)
    comment = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'BIOCHEM-06'


class Biochem07(models.Model):
    assayid = models.ForeignKey('Assay', on_delete=models.CASCADE,related_name='biochem07s')  # Field name made lowercase.
    mid = models.ForeignKey('Mouse', on_delete=models.CASCADE, db_column='mid')
    timepoint = models.IntegerField(blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    measurement_date = models.DateField(blank=True, null=True)
    sample_source = models.CharField(max_length=64, blank=True, null=True)
    iron = models.FloatField(blank=True, null=True)
    uibc = models.FloatField(blank=True, null=True)
    ferritin = models.FloatField(blank=True, null=True)
    transferrin = models.FloatField(blank=True, null=True)
    comment = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'BIOCHEM-07'


class Biochem08(models.Model):
    assayid = models.ForeignKey('Assay', on_delete=models.CASCADE,related_name='biochem08s')  # Field name made lowercase.
    mid = models.ForeignKey('Mouse', on_delete=models.CASCADE, db_column='mid')
    timepoint = models.IntegerField(blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    measurement_date = models.DateField(blank=True, null=True)
    sample_source = models.CharField(max_length=64, blank=True, null=True)
    ldl = models.FloatField(blank=True, null=True)
    creatinine_kinase = models.FloatField(blank=True, null=True)
    potassium = models.FloatField(blank=True, null=True)
    comment = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'BIOCHEM-08'

class Fc01(models.Model):
    assayid = models.ForeignKey('Assay', on_delete=models.CASCADE,related_name='fc01s')  # Field name made lowercase.
    mid = models.ForeignKey('Mouse', on_delete=models.CASCADE, db_column='mid')
    timepoint = models.IntegerField(blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    measurement_date = models.DateField(blank=True, null=True)
    sample_source = models.CharField(max_length=64, blank=True, null=True)
    live_aquis = models.CharField(max_length=64, blank=True, null=True)
    total_cell_count = models.FloatField(blank=True, null=True)
    neu_per = models.FloatField(blank=True, null=True)
    eos_per = models.FloatField(blank=True, null=True)
    mon_per = models.FloatField(blank=True, null=True)
    recent_emigrant_monocytes_per = models.FloatField(blank=True, null=True)
    inflammatory_monocytes_per = models.FloatField(blank=True, null=True)
    steady_state_monocytes_per = models.FloatField(blank=True, null=True)
    nk_cells_per = models.FloatField(blank=True, null=True)
    b_cells_per = models.FloatField(blank=True, null=True)
    t_cells_per = models.FloatField(blank=True, null=True)
    b1b_cells_per = models.FloatField(blank=True, null=True)
    b2b_cells_per = models.FloatField(blank=True, null=True)
    dcs_per = models.FloatField(blank=True, null=True)
    cds_per = models.FloatField(blank=True, null=True)
    cds_cd11_per = models.FloatField(blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    pdcs_per = models.FloatField(blank=True, null=True)
    macrophages_per = models.FloatField(blank=True, null=True)
    class Meta:
        managed = True
        db_table = 'FC-01'

class Fc03(models.Model):
    assayid = models.ForeignKey('Assay', on_delete=models.CASCADE,related_name='fc03s')  # Field name made lowercase.
    mid = models.ForeignKey('Mouse', on_delete=models.CASCADE, db_column='mid')
    timepoint = models.IntegerField(blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    measurement_date = models.DateField(blank=True, null=True)
    sample_source = models.CharField(max_length=64, blank=True, null=True)
    live_aquis = models.CharField(max_length=64, blank=True, null=True)
    total_cell_count = models.FloatField(blank=True, null=True)
    total_b_cells = models.FloatField(blank=True, null=True)
    b1b_cells_per = models.FloatField(blank=True, null=True)
    b2b_cells_per = models.FloatField(blank=True, null=True)
    b2b_immature_cells_per = models.FloatField(blank=True, null=True)
    t1_cells_per = models.FloatField(blank=True, null=True)
    mzb_cells_per = models.FloatField(blank=True, null=True)
    b2_mature_cells_per = models.FloatField(blank=True, null=True)
    t2_cells_per = models.FloatField(blank=True, null=True)
    t3_cells_per = models.FloatField(blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    class Meta:
        managed = True
        db_table = 'FC-03'

class Fc04(models.Model):
    assayid = models.ForeignKey('Assay', on_delete=models.CASCADE,related_name='fc04s')  # Field name made lowercase.
    mid = models.ForeignKey('Mouse', on_delete=models.CASCADE, db_column='mid')
    timepoint = models.IntegerField(blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    measurement_date = models.DateField(blank=True, null=True)
    sample_id = models.CharField(max_length=64, blank=True, null=True)
    sample_source = models.CharField(max_length=64, blank=True, null=True)
    live_aquis = models.CharField(max_length=64, blank=True, null=True)
    total_cell_count = models.FloatField(blank=True, null=True)
    all_cells_per = models.FloatField(blank=True, null=True)
    live_cells_per = models.FloatField(blank=True, null=True)
    early_apoptotic_per = models.FloatField(blank=True, null=True)
    late_apoptotic_per = models.FloatField(blank=True, null=True)
    necrotic_per = models.FloatField(blank=True, null=True)
    all_cells_num = models.DecimalField(max_digits=25, decimal_places=10, blank=True, null=True)
    live_cells_num = models.DecimalField(max_digits=25, decimal_places=10, blank=True, null=True)
    early_apoptotic_num = models.DecimalField(max_digits=25, decimal_places=10, blank=True, null=True)
    late_apoptotic_num = models.DecimalField(max_digits=25, decimal_places=10, blank=True, null=True)
    necrotic_num = models.DecimalField(max_digits=25, decimal_places=10, blank=True, null=True)
    total_leukocytes_per = models.FloatField(blank=True, null=True)
    apoptotic_leukocytes_per = models.FloatField(blank=True, null=True)
    necrotic_leukocytes_per = models.FloatField(blank=True, null=True)
    live_leukocytes_per = models.FloatField(blank=True, null=True)
    total_epithelial_per = models.FloatField(blank=True, null=True)
    apoptotic_epithelial_per = models.FloatField(blank=True, null=True)
    necrotic_epithelial_per = models.FloatField(blank=True, null=True)
    live_epithelial_per = models.FloatField(blank=True, null=True)
    total_leukocytes_num = models.DecimalField(max_digits=25, decimal_places=10, blank=True, null=True)
    apoptotic_leukocytes_num = models.DecimalField(max_digits=25, decimal_places=10, blank=True, null=True)
    necrotic_leukocytes_num = models.DecimalField(max_digits=25, decimal_places=10, blank=True, null=True)
    live_leukocytes_num = models.DecimalField(max_digits=25, decimal_places=10, blank=True, null=True)
    total_epithelial_num = models.DecimalField(max_digits=25, decimal_places=10, blank=True, null=True)
    apoptotic_epithelial_num = models.DecimalField(max_digits=25, decimal_places=10, blank=True, null=True)
    necrotic_epithelial_num = models.DecimalField(max_digits=25, decimal_places=10, blank=True, null=True)
    live_epithelial_num = models.DecimalField(max_digits=25, decimal_places=10, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'FC-04'

class Fc07(models.Model):
    assayid = models.ForeignKey('Assay', on_delete=models.CASCADE,related_name='fc07s')  # Field name made lowercase.
    mid = models.ForeignKey('Mouse', on_delete=models.CASCADE, db_column='mid')
    timepoint = models.IntegerField(blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    measurement_date = models.DateField(blank=True, null=True)
    sample_source = models.CharField(max_length=32, blank=True, null=True)
    facs_lysing = models.CharField(max_length=32, blank=True, null=True)
    live_aquis = models.CharField(max_length=16, blank=True, null=True)
    total_cell_count = models.FloatField(blank=True, null=True)
    neu_per = models.FloatField(blank=True, null=True)
    eos_per = models.FloatField(blank=True, null=True)
    mon_per = models.FloatField(blank=True, null=True)
    ly6chimono_per = models.FloatField(blank=True, null=True)
    ly6cintermono_per = models.FloatField(blank=True, null=True)
    ly6clowmono_per = models.FloatField(blank=True, null=True)
    b_cells_per = models.FloatField(blank=True, null=True)
    cd8_t_per = models.FloatField(db_column='cd8_T_per', blank=True, null=True)  # Field name made lowercase.
    cd4_t_per = models.FloatField(db_column='cd4_T_per', blank=True, null=True)  # Field name made lowercase.
    neu_num = models.FloatField(blank=True, null=True)
    eos_num = models.FloatField(blank=True, null=True)
    mon_num = models.FloatField(blank=True, null=True)
    ly6chimono_num = models.FloatField(blank=True, null=True)
    ly6cintermono_num = models.FloatField(blank=True, null=True)
    ly6clowmono_num = models.FloatField(blank=True, null=True)
    b_cells_num = models.FloatField(blank=True, null=True)
    cd8_t_num = models.FloatField(db_column='cd8_T_num', blank=True, null=True)  # Field name made lowercase.
    cd4_t_num = models.FloatField(db_column='cd4_T_num', blank=True, null=True)  # Field name made lowercase.
    comment = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'FC-07'

class Fc08(models.Model):
    assayid = models.ForeignKey('Assay', on_delete=models.CASCADE,related_name='fc08s')  # Field name made lowercase.
    mid = models.ForeignKey('Mouse', on_delete=models.CASCADE, db_column='mid')
    timepoint = models.IntegerField(blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    measurement_date = models.DateField(blank=True, null=True)
    sample_id = models.CharField(max_length=128, blank=True, null=True)
    sample_source = models.CharField(max_length=64, blank=True, null=True)
    facs_lysing = models.CharField(max_length=32, blank=True, null=True)
    live_aquis = models.CharField(max_length=16, blank=True, null=True)
    total_cell_count = models.FloatField(blank=True, null=True)
    neu_per = models.FloatField(blank=True, null=True)
    eos_per = models.FloatField(blank=True, null=True)
    mon_per = models.FloatField(blank=True, null=True)
    ly6chimono_per = models.FloatField(blank=True, null=True)
    ly6cintermono_per = models.FloatField(blank=True, null=True)
    ly6clowmono_per = models.FloatField(blank=True, null=True)
    dcs_per = models.FloatField(blank=True, null=True)
    nk_cells_per = models.FloatField(blank=True, null=True)
    b_cells_per = models.FloatField(blank=True, null=True)
    t_cells_per = models.FloatField(blank=True, null=True)
    neu_num = models.FloatField(blank=True, null=True)
    eos_num = models.FloatField(blank=True, null=True)
    mon_num = models.FloatField(blank=True, null=True)
    ly6chimono_num = models.FloatField(blank=True, null=True)
    ly6cintermono_num = models.FloatField(blank=True, null=True)
    ly6clowmono_num = models.FloatField(blank=True, null=True)
    dcs_num = models.FloatField(blank=True, null=True)
    nk_cells_num = models.FloatField(blank=True, null=True)
    b_cells_num = models.FloatField(blank=True, null=True)
    t_cells_num = models.FloatField(blank=True, null=True)
    total_cell_count_2 = models.FloatField(blank=True, null=True)
    b_cells_per_2 = models.FloatField(blank=True, null=True)
    nk_cells_per_2 = models.FloatField(blank=True, null=True)
    cd4_per = models.FloatField(blank=True, null=True)
    cd4_cd25_per =models.FloatField(blank=True, null=True)
    #cd4_naive_per =models.FloatField(blank=True, null=True)
    #cd4_eff_per =models.FloatField(blank=True, null=True)
    #cd8_per =models.FloatField(blank=True, null=True)

    comment = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'FC-08'

class Hpni01(models.Model):
    assayid = models.ForeignKey('Assay', on_delete=models.CASCADE, related_name='hpni01s')  # Field name made lowercase.
    mid = models.ForeignKey('Mouse', on_delete=models.CASCADE, db_column='mid')
    timepoint = models.IntegerField(blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    measurement_date = models.DateField(blank=True, null=True)
    avg_score_gray = models.FloatField(blank=True, null=True)
    avg_score_white = models.FloatField(blank=True, null=True)
    total_score = models.FloatField(blank=True, null=True)
    comment = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'HPNI-01'

############################################
#              KOLIARAKI
#############################################

class Pr02(models.Model):
    assayid = models.ForeignKey('Assay', on_delete=models.CASCADE, related_name='pr02s')  # Field name made lowercase.
    mid = models.ForeignKey('Mouse', on_delete=models.CASCADE, db_column='mid')
    timepoint = models.IntegerField(blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    measurement_date = models.DateField(blank=True, null=True)
    mg_feacal_mass = models.FloatField(blank=True, null=True)
    protein_concentration = models.FloatField(blank=True, null=True)
    digestion_protocol = models.CharField(max_length=256, blank=True, null=True)
    amount_injected = models.FloatField(blank=True, null=True)
    lc_ms_analysis_time = models.FloatField(blank=True, null=True)
    instrument_method = models.CharField(max_length=256, blank=True, null=True)
    total_bac_signal = models.FloatField(blank=True, null=True)
    firmicutes_per = models.FloatField(blank=True, null=True)
    bacteroidetes_per = models.FloatField(blank=True, null=True)
    firm_bac_ratio = models.FloatField(blank=True, null=True)
    proteobacteria_per = models.FloatField(blank=True, null=True)
    comment = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'PR-02'

class Cba01(models.Model):
    assayid = models.ForeignKey('Assay', on_delete=models.CASCADE, related_name='cba01s')  # Field name made lowercase.
    mid = models.ForeignKey('Mouse', on_delete=models.CASCADE, db_column='mid')
    timepoint = models.IntegerField(blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    measurement_date = models.DateField(blank=True, null=True)
    dilution_factor = models.FloatField(blank=True, null=True)
    il_six = models.FloatField(blank=True, null=True)
    il_ten = models.FloatField(blank=True, null=True)
    il_twelve = models.FloatField(blank=True, null=True)
    il_seventeen = models.FloatField(blank=True, null=True)
    ifn_gamma = models.FloatField(db_column='ifn-gamma', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    tnf_alpha = models.FloatField(db_column='tnf-alpha', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    comment = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'CBA-01'


class Cba02(models.Model):
    assayid = models.ForeignKey('Assay', on_delete=models.CASCADE, related_name='cba02s')  # Field name made lowercase.
    mid = models.ForeignKey('Mouse', on_delete=models.CASCADE, db_column='mid')
    timepoint = models.IntegerField(blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    measurement_date = models.DateField(blank=True, null=True)
    dilution_factor = models.FloatField(blank=True, null=True)
    igg1 = models.FloatField(blank=True, null=True)
    igg2a = models.FloatField(blank=True, null=True)
    igg3 = models.FloatField(blank=True, null=True)
    iga = models.FloatField(blank=True, null=True)
    igm = models.FloatField(blank=True, null=True)
    igg2b = models.FloatField(blank=True, null=True)
    comment = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'CBA-02'

class Cba03(models.Model):
    assayid = models.ForeignKey('Assay', on_delete=models.CASCADE, related_name='cba03s')  # Field name made lowercase.
    mid = models.ForeignKey('Mouse', on_delete=models.CASCADE, db_column='mid')
    timepoint = models.IntegerField(blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    measurement_date = models.DateField(blank=True, null=True)
    parameter1 = models.FloatField(blank=True, null=True)
    parameter2 = models.FloatField(blank=True, null=True)
    parameter3 = models.FloatField(blank=True, null=True)
    parameter4 = models.TextField(blank=True, null=True)
    comment = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'CBA-03'

class Hpibd01(models.Model):
    assayid = models.ForeignKey('Assay', on_delete=models.CASCADE, related_name='hpibd01s')  # Field name made lowercase.
    mid = models.ForeignKey('Mouse', on_delete=models.CASCADE, db_column='mid')
    timepoint = models.IntegerField(blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    measurement_date = models.DateField(blank=True, null=True)
    colon_length = models.FloatField(blank=True, null=True)
    histology_num = models.FloatField(blank=True, null=True)
    inflammation_score = models.IntegerField(blank=True, null=True)
    tissue_damage_score = models.IntegerField(blank=True, null=True)
    ulceration_score = models.IntegerField(blank=True, null=True)
    involvement_per = models.FloatField(blank=True, null=True)
    total_colitis_score = models.IntegerField(blank=True, null=True)
    tumor_num = models.IntegerField(blank=True, null=True)
    tumor_size = models.FloatField(blank=True, null=True)
    comment = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'HPIBD-01'

class Hpibd03(models.Model):
    assayid = models.ForeignKey('Assay', on_delete=models.CASCADE, related_name='hpibd03s')  # Field name made lowercase.
    mid = models.ForeignKey('Mouse', on_delete=models.CASCADE, db_column='mid')
    timepoint = models.IntegerField(blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    measurement_date = models.DateField(blank=True, null=True)
    histology_num = models.IntegerField(blank=True, null=True)
    si_inflammation_score = models.FloatField(blank=True, null=True)
    colon_inflammation_score = models.FloatField(blank=True, null=True)    
    #goblet_loss = models.FloatField(blank=True, null=True)
    #total_score = models.FloatField(blank=True, null=True)
    #colon_inflammation_score = models.FloatField(blank=True, null=True)
    #colon_goblet_loss = models.FloatField(blank=True, null=True)
    #colon_total_score = models.FloatField(blank=True, null=True)
    comment = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'HPIBD-03'

class Hpibd04(models.Model):
    assayid = models.ForeignKey('Assay', on_delete=models.CASCADE, related_name='hpibd04s')  # Field name made lowercase.
    mid = models.ForeignKey('Mouse', on_delete=models.CASCADE, db_column='mid')
    timepoint = models.IntegerField(blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    measurement_date = models.DateField(blank=True, null=True)
    slide_number = models.IntegerField(blank=True, null=True)
    leukocyte_density_1 = models.FloatField(blank=True, null=True)
    leukocyte_density_2 = models.FloatField(blank=True, null=True)
    leukocyte_density_3 = models.FloatField(blank=True, null=True)
    leukocyte_density_avg = models.FloatField(blank=True, null=True)
    level_1 = models.FloatField(blank=True, null=True)
    level_2 = models.FloatField(blank=True, null=True)
    level_3 = models.FloatField(blank=True, null=True)
    level_avg = models.FloatField(blank=True, null=True)    
    extent_1 = models.FloatField(blank=True, null=True)
    extent_2 = models.FloatField(blank=True, null=True)
    extent_3 = models.FloatField(blank=True, null=True)
    extent_avg = models.FloatField(blank=True, null=True)    
    inflammation_score = models.FloatField(blank=True, null=True)
    abscesses = models.FloatField(blank=True, null=True)
    comment = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'HPIBD-04'

class Endo01(models.Model):
    assayid = models.ForeignKey('Assay', on_delete=models.CASCADE, related_name='endo01s')  # Field name made lowercase.
    mid = models.ForeignKey('Mouse', on_delete=models.CASCADE, db_column='mid')
    timepoint = models.IntegerField(blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    measurement_date = models.DateField(blank=True, null=True)
    thicken_colon = models.FloatField(blank=True, null=True)
    changes_vascular = models.CharField(max_length=255, blank=True, null=True)
    fibrin_visible = models.FloatField(blank=True, null=True)
    granularity_mucosak = models.FloatField(blank=True, null=True)
    stool_consistency = models.FloatField(blank=True, null=True)
    total_colitis_score = models.FloatField(blank=True, null=True)
    num_tumor_size_1 = models.FloatField(blank=True, null=True)
    num_tumor_size_2 = models.FloatField(blank=True, null=True)
    num_tumor_size_3 = models.FloatField(blank=True, null=True)
    num_tumor_size_4 = models.FloatField(blank=True, null=True)
    num_tumor_size_5 = models.FloatField(blank=True, null=True)
    total_tumor_num = models.FloatField(blank=True, null=True)
    tumor_load = models.FloatField(blank=True, null=True)
    comment = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'ENDO-01'
############################################
#              ARMAKA
#############################################

class Ar02(models.Model):
    assayid = models.ForeignKey('Assay', on_delete=models.CASCADE, related_name='ar02s')  # Field name made lowercase.
    mid = models.ForeignKey('Mouse', on_delete=models.CASCADE, db_column='mid')
    timepoint = models.IntegerField(blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    measurement_date = models.DateField(blank=True, null=True)
    parameter1 = models.FloatField(blank=True, null=True)
    parameter2 = models.FloatField(blank=True, null=True)
    parameter3 = models.FloatField(blank=True, null=True)
    parameter4 = models.TextField(blank=True, null=True)
    comment = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'AR-02'

class Ar03(models.Model):
    assayid = models.ForeignKey('Assay', on_delete=models.CASCADE, related_name='ar03s')  # Field name made lowercase.
    mid = models.ForeignKey('Mouse', on_delete=models.CASCADE, db_column='mid')
    timepoint = models.IntegerField(blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    measurement_date = models.DateField(blank=True, null=True)
    sum_intensity_fl = models.FloatField(verbose_name ="sum intensity (FL)", blank=True, null=True)
    net_intensity_fl = models.FloatField(blank=True, null=True)
    sum_intensity_hl = models.FloatField(blank=True, null=True)
    net_intensity_hl = models.FloatField(blank=True, null=True)
    sum_intensity_total = models.FloatField(blank=True, null=True)
    net_intensity_total = models.FloatField(blank=True, null=True)
    acquisition_settings = models.TextField(blank=True, null=True)
    comment = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'AR-03'

class Ar04(models.Model):
    assayid = models.ForeignKey('Assay', on_delete=models.CASCADE, related_name='ar04s')  # Field name made lowercase.
    mid = models.ForeignKey('Mouse', on_delete=models.CASCADE, db_column='mid')
    timepoint = models.IntegerField(blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    measurement_date = models.DateField(blank=True, null=True)
    sum_intensity = models.FloatField(blank=True, null=True)
    net_intensity = models.FloatField(blank=True, null=True)
    mean_intensity = models.FloatField(blank=True, null=True)
    acquisition_settings = models.TextField(blank=True, null=True)
    comment = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'AR-04'

class Ar05(models.Model):
    assayid = models.ForeignKey('Assay', on_delete=models.CASCADE, related_name='ar05s')  # Field name made lowercase.
    mid = models.ForeignKey('Mouse', on_delete=models.CASCADE, db_column='mid')
    timepoint = models.IntegerField(blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    measurement_date = models.DateField(blank=True, null=True)
    bvtv = models.FloatField(blank=True, null=True)
    bstv = models.FloatField(blank=True, null=True)
    trabecular_thickness = models.FloatField(blank=True, null=True)
    trabecular_number = models.FloatField(blank=True, null=True)
    trabecular_seperation = models.FloatField(blank=True, null=True)
    comment = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'AR-05'

class Ar06(models.Model):
    assayid = models.ForeignKey('Assay', on_delete=models.CASCADE, related_name='ar06s')  # Field name made lowercase.
    mid = models.ForeignKey('Mouse', on_delete=models.CASCADE, db_column='mid')
    timepoint = models.IntegerField(blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    measurement_date = models.DateField(blank=True, null=True)
    clinical_score = models.FloatField(blank=True, null=True)
    comment = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'AR-06'

class Ar07(models.Model):
    assayid = models.ForeignKey('Assay', on_delete=models.CASCADE, related_name='ar07s')  # Field name made lowercase.
    mid = models.ForeignKey('Mouse', on_delete=models.CASCADE, db_column='mid')
    timepoint = models.IntegerField(blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    measurement_date = models.DateField(blank=True, null=True)
    weight = models.FloatField(blank=True, null=True)
    comment = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'AR-07'

class Hpa02(models.Model):
    assayid = models.ForeignKey('Assay', on_delete=models.CASCADE, related_name='hpa02s')  # Field name made lowercase.
    mid = models.ForeignKey('Mouse', on_delete=models.CASCADE, db_column='mid')
    timepoint = models.IntegerField(blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    measurement_date = models.DateField(blank=True, null=True)
    synovitis = models.FloatField(blank=True, null=True)
    cartilage_destruction = models.FloatField(blank=True, null=True)
    bone_erosion = models.FloatField(blank=True, null=True)
    comment = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'HPA-02'


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

'''mouselist = measures.values('mid').distinct().order_by('mid')
gender = Mouse.objects.filter(id__in=mouselist).values_list('gender', flat=True).distinct()
genotype = Mouse.objects.filter(id__in=mouselist).values_list('genotype', flat=True).distinct()
#treated = Mouse.objects.filter(id__in=mouselist).values_list('treated', flat=True).distinct()
#induced = Mouse.objects.filter(id__in=mouselist).values_list('induced', flat=True).distinct()
pars = get_parameters(a)
for parameter in pars:
def parameterMeasures(measures, parameter):
    mouselist = measures.values('mid').distinct().order_by('mid')
    gender = Mouse.objects.filter(id__in=mouselist).values_list('gender', flat=True).distinct()
    genotype = Mouse.objects.filter(id__in=mouselist).values_list('genotype', flat=True).distinct()
    test = {}
    for sex in gender:
        for gene in genotype:
            label = sex + " "+gene
            m = Mouse.objects.filter(id__in= mouselist,genotype=gene,gender=sex)
            parameter_measures = measures.filter(mid__in = m).values_list('timepoint',parameter)
            df = pd.DataFrame(list(parameter_measures.values('timepoint', parameter)))
            test[label] = df
    return test
test = parameterMeasures(measures,pars[0])
'''
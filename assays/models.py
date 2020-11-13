from django.db import models
from django.contrib.auth.models import User

from pipelines.models import Pipeline
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
    pipeline = models.ForeignKey(Pipeline, on_delete=models.DO_NOTHING, related_name='assays',blank=True, null=True)
    updated_by = models.ForeignKey(User,on_delete=models.DO_NOTHING, related_name='updated_by_user',blank=True, null=True)
    scientist = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name="scientists",related_query_name="scientist",blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def get_absolute_url(self):
        return reverse('assay-detail', kwargs={'pk': self.pk})

    def __str__(self):
        return u'{0}\t\t{1}'.format(self.name, self.code)

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


class Fc04(models.Model):
    assayid = models.ForeignKey('Assay', on_delete=models.CASCADE,related_name='fc04s')  # Field name made lowercase.
    mid = models.ForeignKey('Mouse', on_delete=models.CASCADE, db_column='mid')
    timepoint = models.IntegerField(blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    measurement_date = models.DateField(blank=True, null=True)
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
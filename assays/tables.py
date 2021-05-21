from django_tables2_column_shifter.tables import ColumnShiftTable
from .models import *

class Ni02Rot01Table(ColumnShiftTable):
    class Meta:
        model = Ni02Rot01
        template_name = 'django_tables2/bootstrap4.html'

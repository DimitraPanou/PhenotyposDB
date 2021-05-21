import django_filters
from django_filters import DateFilter, CharFilter,ModelChoiceFilter
from django.contrib.auth.models import User

from .models import *

class AtypeFilter(django_filters.FilterSet):
	class Meta:
		model = Atype
		fields = ['facility','unit']


class AssayFilter(django_filters.FilterSet):
	start_date = DateFilter(field_name="measurement_day", lookup_expr='gte')
	end_date = DateFilter(field_name="measurement_day", lookup_expr='lte')
	name = CharFilter(field_name='name', lookup_expr='contains')
	author = ModelChoiceFilter(field_name='author',queryset=User.objects.all())
	class Meta:
		model = Assay
		fields = '__all__'
		exclude = ['code','measurement_day','version', 'comments','rawdata_file','assayqc','pipeline','updated_by','scientist','created_at','updated_at','mouse_age','duration','timesteps_in']
		'''widgets = {
        'start_date': forms.DateInput(format=('%Y-%m-%d'), attrs={'placeholder':'Select a date', 'type':'date'}),
    	}'''


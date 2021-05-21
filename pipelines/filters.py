import django_filters
from django_filters import DateFilter, CharFilter,ModelChoiceFilter
from django.contrib.auth.models import User

from .models import *

class PipelinetypeFilter(django_filters.FilterSet):
	class Meta:
		model = PipelineType
		fields = '__all__'


class PipelineFilter(django_filters.FilterSet):
	start_date = DateFilter(field_name="pip_start")
	end_date = DateFilter(field_name="pip_end")
	name = CharFilter(field_name='name', lookup_expr='contains')
	pi = ModelChoiceFilter(field_name='pi',queryset=User.objects.all())
	class Meta:
		model = Pipeline
		fields = ['name','model','status']

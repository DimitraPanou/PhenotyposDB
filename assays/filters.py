import django_filters
from django import forms

from django_filters import DateFilter, CharFilter,ModelChoiceFilter
from django.contrib.auth.models import User

from .models import *

class AtypeFilter(django_filters.FilterSet):
	class Meta:
		model = Atype
		fields = ['facilitylong','service_type']


class AssayFilter(django_filters.FilterSet):
	start_date = DateFilter(field_name="measurement_day", lookup_expr='gte',widget=forms.DateInput(format=('%Y-%m-%d'), attrs={'placeholder':'Select a date', 'type':'date'}))
	end_date = DateFilter(field_name="measurement_day", lookup_expr='lte',widget=forms.DateInput(format=('%Y-%m-%d'), attrs={'placeholder':'Select a date', 'type':'date'}))
	name = CharFilter(field_name='name', lookup_expr='contains')
	author = ModelChoiceFilter(field_name='author',queryset=User.objects.all(), widget=forms.Select(attrs={'class': 'form-control select2'}))
	scientist_in_charge = ModelChoiceFilter(field_name='scientist_in_charge',queryset=User.objects.all(),widget=forms.Select(attrs={'class': 'form-control select2'}))
	type = ModelChoiceFilter(field_name='type',queryset=Atype.objects.all(),widget=forms.Select(attrs={'class': 'form-control select2'}))

	class Meta:
		model = Assay
		fields = '__all__'
		exclude = ['code','measurement_day','version', 'comments','rawdata_file','assayqc','pipeline','updated_by','members','created_at','updated_at','mouse_age','duration','timesteps_in']

class MouseFilter(django_filters.FilterSet):
	gender = ModelChoiceFilter(field_name='gender',queryset=Mouse.objects.all())
	class Meta:
		model = Mouse
		fields = '__all__'
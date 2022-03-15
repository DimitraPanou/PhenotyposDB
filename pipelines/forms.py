from django import forms
#from .models import Assays
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column
from .models import PipelineType, Pipeline
from bootstrap_modal_forms.forms import BSModalModelForm
class PipelineForm(forms.ModelForm):
    class Meta:
        model = Pipeline
        exclude = ('pi',)
        fields = ('name', 'model','protocol','pip_start','pip_end','status','pipelineqc','type')
        widgets = {
        'pip_start': forms.DateInput(format=('%d/%m/%Y'), attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date'}),
        'pip_end': forms.DateInput(format=('%d/%m/%Y'), attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date'}),
        'type': forms.Select(attrs={'class':'form-control select2'}),
        'status': forms.Select(attrs={'class':'form-control select2'})        
    	}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            'name',
            Row(
                Column('model', css_class='form-group col-md-6 mb-0'),
                Column('type', css_class='form-control select2'),
                Column('protocol', css_class='form-group col-md-6 mb-0'),                
                css_class='form-row'
            ),
            Row(    
                Column('pip_start', css_class='form-group col-md-6 mb-0'),
                Column('pip_end', css_class='form-group col-md-6 mb-0'),
                Column('status', css_class='form-control select2'),                
                css_class='form-row'
            ),


            Submit('submit', 'Add')
        )


class PipelineTypeForm(forms.ModelForm):
    class Meta:
        model = PipelineType
        fields = ('code', 'name')


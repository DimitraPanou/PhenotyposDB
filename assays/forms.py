from django import forms
#from .models import Assays
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column
from .models import Atype, Assay

class AssayForm(forms.ModelForm):
    class Meta:
        model = Assay
        exclude = ('author',)
        fields = ('code', 'name', 'version','staff','comments','measurement_day','rawdata_file','assayqc','type')
        widgets = {
        'measurement_day': forms.DateInput(format=('%d/%m/%Y'), attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date'}),
    	}

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class AtypeForm(forms.ModelForm):
    class Meta:
        model = Atype
        fields = ('code', 'name', 'facility','unit','staff','publication_date','version')
        widgets = {
        'publication_date': forms.DateInput(format=('%m/%d/%Y'), attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date'}),
    	}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column('code', css_class='form-group col-md-6 mb-0'),
                Column('name', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            'facility',
            'unit',
            Row(
                Column('staff', css_class='form-group col-md-6 mb-0'),
                Column('publication_date', css_class='form-group col-md-4 mb-0'),
                Column('version', css_class='form-group col-md-2 mb-0'),
                css_class='form-row'
            ),
            Submit('submit', 'Add')
        )


class AtypeExtraForm(forms.ModelForm):
    class Meta:
        model = Atype
        fields = ('assay_word','purpose','experimental_design','equipment','supplies','procedures','troubleshooting','appendix','references')

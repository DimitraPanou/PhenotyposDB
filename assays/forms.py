from django import forms
#from .models import Assays
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column
from .models import Atype, Assay, AssociatedImage

class AssayForm(forms.ModelForm):
    class Meta:
        model = Assay
        exclude = ('author',)
        fields = ('code', 'name','type','version','staff','measurement_day','mouse_age','duration','timesteps_in','scientist','assayqc','rawdata_file','comments')
        widgets = {
        'name': forms.TextInput(attrs={'class':'input'}),
        'rawdata_file': forms.FileInput(attrs={'class':'dropify'}),
        'measurement_day': forms.DateInput(format=('%Y-%m-%d'), attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date','useCurrent': True}),
        'type': forms.Select(attrs={'class':'form-control select2'}),
        'timesteps_in': forms.Select(attrs={'class':'form-control select2'}),
        'scientist': forms.Select(attrs={'class':'form-control select2'}),
        'mouse_age': forms.Select(attrs={'class':'form-control select2'})
    	}
    def __init__(self, user, *args, **kwargs):
        super(AssayForm,self).__init__(*args, **kwargs)
        print('inside form')
        print(user)
        if(user.groups.all()[0].name =='Admin' or user.groups.all()[0].name =='Scientific staff'):
            self.fields['type'].queryset = Atype.objects.all()
        else:
            self.fields['type'].queryset = Atype.objects.filter(facilitylong = user.profile.facility)
        
#        def save(self,user, *args, **kwargs):
#        form = super(AssayForm, self).save(*args, **kwargs)
#        return form


'''class ChoiceForm(forms.Form):
    Countries = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,
                                          choices=OPTIONS)
   '''
class Assay2Form(forms.ModelForm):
    class Meta:
        model = Assay
        exclude = ('author',)
        fields = ('code', 'name','version','staff','measurement_day','mouse_age','duration','timesteps_in','scientist','assayqc','rawdata_file','comments')
        widgets = {
        'name': forms.TextInput(attrs={'class':'input'}),
        'rawdata_file': forms.FileInput(attrs={'class':'dropify'}),
        'measurement_day': forms.DateInput(format=('%Y-%m-%d'), attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date','useCurrent': True}),
        'timesteps_in': forms.Select(attrs={'class':'form-control select2'}),
        'scientist': forms.Select(attrs={'class':'form-control select2'}),
        'mouse_age': forms.Select(attrs={'class':'form-control select2'})
        }

#'data-default-file': self.rawdata_file
class AtypeForm(forms.ModelForm):
    class Meta:
        model = Atype
        fields = ('code', 'name', 'facility','facilitylong','unit','staff','publication_date','version')
        widgets = {
        'publication_date': forms.DateInput(format=('%Y-%m-%d'), attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date','useCurrent': True}),
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
            'facilitylong',
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
        widgets = {
        'assay_word': forms.FileInput(attrs={'class':'dropify','useCurrent': True}),
        }

class ImageForm(forms.ModelForm):
    class Meta:
        model = AssociatedImage
        fields = ['title','image','caption']
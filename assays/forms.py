from django import forms
#from .models import Assays
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column
from .models import Atype, Assay, AssociatedImage, Report

class AssayForm(forms.ModelForm):
    class Meta:
        model = Assay
        exclude = ('author',)
        fields = ('code', 'name','type','version','staff','measurement_day','mouse_age','duration','timesteps_in','scientist_in_charge','assayqc','rawdata_file','comments')
        widgets = {
        'name': forms.TextInput(attrs={'class':'input'}),
        'rawdata_file': forms.FileInput(attrs={'class':'dropify'}),
        'measurement_day': forms.DateInput(format=('%Y-%m-%d'), attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date','useCurrent': True}),
        'type': forms.Select(attrs={'class':'form-control select2'}),
        'timesteps_in': forms.Select(attrs={'class':'form-control select2'}),
        'scientist_in_charge': forms.Select(attrs={'class':'form-control select2'}),
        'members': forms.SelectMultiple(attrs={'class':'select2'}),
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
        #self.fields['members'].queryset = User.objects.all()
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
        exclude = ('author','rawdata_file')
        fields = ('code', 'name','version','staff','measurement_day','mouse_age','duration','timesteps_in','scientist_in_charge','members','assayqc','comments')
        widgets = {
        'name': forms.TextInput(attrs={'class':'input'}),
        #'rawdata_file': forms.FileInput(attrs={'class':'dropify'}),
        'measurement_day': forms.DateInput(format=('%Y-%m-%d'), attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date','useCurrent': True}),
        'timesteps_in': forms.Select(attrs={'class':'form-control select2'}),
        'scientist_in_charge': forms.Select(attrs={'class':'form-control select2'}),
        'members': forms.SelectMultiple(attrs={'class':'select2'}),
        'mouse_age': forms.Select(attrs={'class':'form-control select2'})
        }
    def save(self, commit=True):
        form = super().save(commit=False)
        print("User members")
        #print form['members'].value()
        #if not form.instance.id:
            #form.instance= Assay.objects.get()
        #form = super(Assay2Form, self).save(*args, **kwargs)
        if commit:
            form.save()
            self.save_m2m()
        return form
#'data-default-file': self.rawdata_file
class AtypeForm(forms.ModelForm):
    class Meta:
        model = Atype
        fields = ('code', 'name','facilitylong','service_type','staff','publication_date','version')
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
            'facilitylong',
            'service_type',
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

class ReportForm(forms.ModelForm):
    class Meta:
        model = Report
        fields = ['name','introduction','summary','reportassay']
        widgets = {
            'name': forms.TextInput(attrs={'class':'input'}),
            'reportassay': forms.Select(attrs={'class':'form-control select2'}),
            }
    def __init__(self, user, *args, **kwargs):
        super(ReportForm,self).__init__(*args, **kwargs)
        self.fields['reportassay'].queryset = Assay.objects.all()
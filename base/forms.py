from django import forms
#from .models import Assays
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('title', 'author', 'pdf', 'cover')

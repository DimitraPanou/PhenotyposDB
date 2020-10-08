# Create your views here.

from django.shortcuts import render, redirect,get_object_or_404
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
    TemplateView
)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User

from django.urls import reverse_lazy
#from .forms import AssayForm
from .forms import AssayForm, AtypeForm, AtypeExtraForm
from .models import Assay, Atype
from django.views.generic import DetailView
from django.views.generic.edit import FormMixin
from django.views.generic import FormView

from .functions import handle_uploaded_file, returnTemplateName
####################
#    Assays        #
####################

class AssaysListView(ListView):
	model = Assay
	template_name = 'assays/assays.html'
	context_object_name = 'list_assays'

#class AssaysCreateView(LoginRequiredMixin,CreateView):
#	model = Assay
#	template_name = 'assays/add_assay.html'
#	form_class = AssayForm
#	success_url = '/assays/'

#	def form_valid(self, form):
#		form.instance.author = self.request.user
#		return super().form_valid(form)


def add_assay(request, *args, **kargs):
    if request.method == 'POST':
        form = AssayForm(request.POST, request.FILES)
        if form.is_valid():
            form.instance.author = request.user
            test = form.save()
            #for filename, file in request.FILES.items():
            #    name = request.FILES[filename].url
                #print(name)
            print(test.rawdata_file.url)
            handle_uploaded_file(test)
            return redirect('assays')
    else:
        form = AssayForm()
    return render(request, 'assays/add_assay.html', {
        'form': form
    })

class AssaysUpdateView(LoginRequiredMixin,UpdateView):
	model = Assay
	template_name = 'assays/update_assay.html'
	form_class = AssayForm
	success_url = '/assays/'

	def form_valid(self, form):
		form.instance.updated_by = self.request.user
		return super().form_valid(form)	

class AssaysDeleteView(DeleteView):
	model = Assay
	template_name = 'assays/delete_assay.html'
	success_url = reverse_lazy('assays')


class AssaysDetailView(DetailView):
	model = Assay
	#template_name = 'assays/assaytypes/iinflc-04.html'
	#template_name = returnTemplateName(self.object)

	def get_template_names(self):
		print(self.object.type)
		#return ['assays/assaytypes/ni01.html','assays/assaytypes/iinflc-04.html']
		return returnTemplateName(self.object.type)

	def get_context_data(self, **kwargs):
		switcher ={
			5: self.get_object().iinflc04s.annotate(),
			7: self.get_object().ni01s.annotate(),
			8: self.get_object().ni02rot01s.annotate(),
			9: self.get_object().ni02ofd01s.annotate()
		}
		kwargs['measures'] = switcher.get(self.object.type.id,"Ivalid")
		return super().get_context_data(**kwargs)


class UserAssaysListView(LoginRequiredMixin,ListView):
	model = Assay
	template_name = 'assays/assays.html'
	context_object_name = 'list_assays'

	def get_queryset(self):
		user = get_object_or_404(User,username=self.kwargs.get('username'))
		return Assay.objects.filter(author=user).order_by('measurement_day')

	def get_context_data(self, **kwargs):
		kwargs['flag'] = 1
		return super().get_context_data(**kwargs)


class GroupAssaysListView(LoginRequiredMixin,ListView):
	model = Assay
	template_name = 'assays/assays.html'
	context_object_name = 'list_assays'

	def get_queryset(self):
		user = get_object_or_404(User,username=self.kwargs.get('username'))
		return Assay.objects.filter(scientist=user).order_by('measurement_day')

	def get_context_data(self, **kwargs):
		kwargs['flag2'] = 1
		return super().get_context_data(**kwargs)
#################################
# TYPES
#################################

class AtypeListView(ListView):
	model = Atype
	template_name = 'assays/assaytypes.html'
	context_object_name = 'list_assays'

'''
class AtypeCreateView(LoginRequiredMixin,CreateView):
	model = Atype
	template_name = 'assays/add_assay.html'
	form_class = AtypeForm
	success_url = '/assays/'

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)
'''
def add_atype(request, *args, **kargs):
    a=Assay()	
    if request.method == 'POST':
        form = AtypeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('atypes')
    else:
        form = AtypeForm()
    return render(request, 'assays/add_assaytype.html', {
        'form': form,
        'a': a
    })

class AtypeUpdateView(UpdateView):
	model = Atype
	template_name = 'assays/update_assaytype.html'
	form_class = AtypeForm
	success_url = '/assays/types/'

class AtypeDeleteView(DeleteView):
	model = Atype
	template_name = 'assays/delete_assaytype.html'
	success_url = '/assays/types/'


class AtypeDetailView(DetailView):
	model = Atype
	template_name = 'assays/assaytype_page.html'

#Need to fix this
class Atype2UpdateView(UpdateView):
	model = Atype
	template_name = 'assays/update_assaytype2.html'
	form_class = AtypeExtraForm

	def get_success_url(self):
		return(reverse_lazy('assaytype-detail', kwargs={'pk': self.object.id}))

'''
	def post(self,request,pk,*args,**kwargs):
		obj = get_object_or_404(Atype, id=pk)
		form = AtypeExtraForm(request,POST, instance=obj)
		print(form)
		if form.is_valid():
			form.save()
'''

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
from .forms import PipelineForm, PipelineTypeForm
from .models import Pipeline, PipelineType
from django.views.generic import DetailView
from django.views.generic.edit import FormMixin
from django.views.generic import FormView

from assays.models import Assay
from assays.forms import AssayForm
from assays.functions import handle_uploaded_file
####################
#    Pipelines     #
####################

class PipelineListView(ListView):
	model = Pipeline
	template_name = 'pipelines/pipelines.html'
	context_object_name = 'list_pipelines'

#Authenticate scientist here
def add_pipeline(request, *args, **kargs):
    if request.method == 'POST':
        form = PipelineForm(request.POST, request.FILES)
        if form.is_valid():
            form.instance.pi = request.user
            test = form.save()
            return redirect('pipelines')
    else:
        form = PipelineForm()
    return render(request, 'pipelines/add_pipeline.html', {
        'form': form
    })

class PipelineUpdateView(LoginRequiredMixin,UpdateView):
	model = Pipeline
	template_name = 'pipelines/update_pipeline.html'
	form_class = PipelineForm
	success_url = reverse_lazy('pipelines')

	def get_queryset(self):
		return self.request.user.pipelines.all()

	def form_valid(self, form):
	#	form.instance.updated_by = self.request.user
		return super().form_valid(form)	

class PipelineDeleteView(DeleteView):
	model = Pipeline
	template_name = 'pipelines/delete_pipeline.html'
	success_url = reverse_lazy('pipelines')


class UserPipelineListView(LoginRequiredMixin,ListView):
	model = Pipeline
	template_name = 'pipelines/user-pipelines.html'
	context_object_name = 'list_pipelines'

	def get_queryset(self):
		user = get_object_or_404(User,username=self.kwargs.get('username'))
		return Pipeline.objects.filter(pi=user).order_by('created_at')

	def get_context_data(self, **kwargs):
		kwargs['flag_pipeline'] = 1
		return super().get_context_data(**kwargs)


#Authenticate scientist here

class PipelineDetailView(DetailView):
	model = Pipeline
	template_name = 'pipelines/detail_pipeline.html'

	def get_context_data(self, **kwargs):
		kwargs['assays'] = self.get_object().assays.annotate()		
		return super().get_context_data(**kwargs)

'''
class UserAssaysListView(LoginRequiredMixin,ListView):
	model = Assay
	template_name = 'assays/assays.html'
	context_object_name = 'list_assays'

	def get_queryset(self):
		user = get_object_or_404(User,username=self.kwargs.get('username'))
		return Assay.objects.filter(author=user).order_by('measurement_day')
'''
#################################
# TYPES
#################################

class PipelineTypeListView(ListView):
	model = PipelineType
	template_name = 'pipelines/pipelinetypes.html'
	context_object_name = 'list_pipelines'


def add_pipelinetype(request, *args, **kargs):
    if request.method == 'POST':
        form = PipelineForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('pipelinetypes')
    else:
        form = PipelineForm()
    return render(request, 'pipelines/add_pipelinetype.html', {
        'form': form,
        'a': a
    })

class PipelineTypeUpdateView(UpdateView):
	model = PipelineType
	template_name = 'pipelines/update_pipelinetype.html'
	form_class = PipelineTypeForm
	success_url = '/pipelines/types/'

class PipelineTypeDeleteView(DeleteView):
	model = PipelineType
	template_name = 'pipelines/delete_pipelinetype.html'
	success_url = '/pipelines/types/'

def add_assay_to_pipeline(request, pk):
	pipeline = get_object_or_404(Pipeline, pk=pk, pi=request.user)
	if request.method == 'POST':
		form = AssayForm(request.POST, request.FILES)
		if form.is_valid():
			form.instance.pipeline = pipeline
			form.instance.author = request.user			
			test = form.save()
			handle_uploaded_file(test)			
			return redirect('pipelines')
	else:
		form = AssayForm()
	return render(request,'pipelines/add_assay.html',{'pipeline':pipeline, 'form':form})

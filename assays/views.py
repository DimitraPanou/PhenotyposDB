# Create your views here.
import json
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
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required
from users.decorators import allowed_users

from django.urls import reverse_lazy
#from .forms import AssayForm
from .forms import AssayForm, AtypeForm, AtypeExtraForm, ImageForm
from .models import Assay, Atype, Mouse
from django.views.generic import DetailView
from django.views.generic.edit import FormMixin
from django.views.generic import FormView

from .functions import handle_uploaded_file, returnTemplateName

from django.db.models import Count

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


@allowed_users(allowed_roles=['Admin','Scientific staff','Lab member'])
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
            if(handle_uploaded_file(test)==-1):
                    html = "<html><body>Problem with the file.</body></html>"
                    return HttpResponse(html)
            return redirect('assays')
    else:
        form = AssayForm()
    return render(request, 'assays/add_assay.html', {
        'form': form
    })

@allowed_users(allowed_roles=['Admin','Scientific staff','Lab member'])
def uploadImage(request, *args, **kargs):
	assay = get_object_or_404(Assay, pk=pk, pi=request.user)
	if request.method == 'POST':
		form = ImageForm(request.POST, request.FILES)
		if form.is_valid():
			form.instance.assayid = assay
			test = form.save()
			if(handle_uploaded_file(test)==-1):
				html = "<html><body>Problem with the file.</body></html>"
				return HttpResponse(html)
			return redirect('assays')
		else:
			form = ImageForm()
	return render(request, 'assays/detail_assay2.html', {'object':assay, 'imageform':form})

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
			4: self.get_object().iinflc03s.annotate(),
			5: self.get_object().iinflc04s.annotate(),
			6: self.get_object().iinflc02s.annotate(),
			7: self.get_object().ni01s.annotate(),
			8: self.get_object().ni02rot01s.annotate(),
			9: self.get_object().ni02ofd01s.annotate(),
			10: self.get_object().ni02grs01s.annotate(),
			11: self.get_object().hem01s.annotate(),
			12: self.get_object().hpibd02s.annotate(),
			13: self.get_object().biochem01s.annotate(),
			14: self.get_object().biochem02s.annotate(),
			15: self.get_object().biochem03s.annotate(),
			16: self.get_object().biochem04s.annotate(),
			17: self.get_object().biochem05s.annotate(),
			18: self.get_object().biochem06s.annotate(),
			19: self.get_object().biochem07s.annotate(),
			20: self.get_object().biochem08s.annotate(),
			22: self.get_object().hpni01s.annotate(),
			23: self.get_object().fc08s.annotate(),
			24: self.get_object().ar02s.annotate(),

		}
		# mouselist = i4.values('mid').distinct().order_by('mid')
		# objects = Mouse.objects.filter(id__in=mouselist)
		#images = self.get_object().associated_images.annotate()
		measures = switcher.get(self.object.type.id,"Ivalid")
		kwargs['measures'] = measures
		mouselist = measures.values('mid').distinct().order_by('mid')
		mouse_num = measures.values('mid').annotate(dcount=Count('mid')).count()	
		females = 	Mouse.objects.filter(id__in=mouselist).filter(gender='Female')
		males = 	Mouse.objects.filter(id__in=mouselist).filter(gender='Male')
		kwargs['mouselist'] = Mouse.objects.filter(id__in=mouselist)
		kwargs['total'] = mouse_num
		kwargs['assayjson']= json.dumps(self.object.id)
		kwargs['females'] = females.count()
		kwargs['males'] = males.count()
		return super().get_context_data(**kwargs)


class UserAssaysListView(LoginRequiredMixin,ListView):
	model = Assay
	template_name = 'assays/user-assays.html'
	context_object_name = 'list_assays'

	def get_queryset(self):
		user = get_object_or_404(User,username=self.kwargs.get('username'))
		a= Assay.objects.filter(author=user).order_by('measurement_day')
		b= Assay.objects.filter(scientist=user).order_by('measurement_day')		
		return a|b
	def get_context_data(self, **kwargs):
		kwargs['flag'] = 1
		return super().get_context_data(**kwargs)


class GroupAssaysListView(LoginRequiredMixin,ListView):
	model = Assay
	template_name = 'assays/user-assays.html'
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

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
from .forms import AssayForm, Assay2Form, AtypeForm, AtypeExtraForm, ImageForm
from .models import Assay, Atype, Mouse
from django.views.generic import DetailView
from django.views.generic.edit import FormMixin
from django.views.generic import FormView

from .functions import handle_uploaded_file, returnTemplateName, get_parameters, parameterMeasures
from .filters import AssayFilter
from django.db.models import Count

####################
#    Assays        #
####################


def assayslist(request):
	myFilter = AssayFilter(request.GET)
	assays = myFilter.qs 
	for assay in assays:
		print(len(returnMeasurements(assay)))
		assay.counter = len(returnMeasurements(assay))
	context = {'list_assays':assays,
	'myFilter':myFilter}
	return render(request, 'assays/assays.html',context)

class AssaysListView(ListView):
	model = Assay
	template_name = 'assays/assays.html'
	context_object_name = 'list_assays'

	def get_context_data(self, **kwargs):
		assays = Assay.objects.all()
		myFilter = AssayFilter(request.GET, queryset=assays)
		kwargs['myFilter'] = myFilter
		return super().get_context_data(**kwargs)
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
        form = AssayForm(request.user,request.POST, request.FILES)
        if form.is_valid():
            form.instance.author = request.user
            print(request.user.profile.first_name)
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
        form = AssayForm(request.user)
    return render(request, 'assays/add_assay.html', {
        'form': form
    })

@allowed_users(allowed_roles=['Admin','Scientific staff','Lab member'])
def uploadImage(request, pk):
	#assay = get_object_or_404(Assay, pk=pk)
	if request.method == 'POST':
		form = ImageForm(request.POST, request.FILES)
		if form.is_valid():
			#form.instance.assayid = assay
			test = form.save()
			if(handle_uploaded_file(test)==-1):
				html = "<html><body>Problem with the file.</body></html>"
				return HttpResponse(html)
			return redirect('uploadImage')
			#return(reverse_lazy('assaytype-detail', kwargs={'pk': self.assay.id}))
		else:
			form = ImageForm()
	return render(request, 'assays/imageupload.html', {'imageform':form})

@allowed_users(allowed_roles=['Admin','Scientific staff','Lab member'])
def updateAssay(request, pk):
	assay = Assay.objects.get(id=pk)
	form = AssayForm(request.user,request.FILES, instance=assay)

	if request.method == 'POST':
		form = AssayForm(request.user,request.POST, request.FILES, instance=assay)
		if form.is_valid():
			form.instance.updated_by = self.request.user
			form.save()
			return redirect('assays')

	context = {'form':form}
	return render(request, 'assays/update_assay.html', context)

class AssaysUpdateView(LoginRequiredMixin,UpdateView):
	model = Assay
	template_name = 'assays/update_assay.html'
	form_class = Assay2Form
	success_url = '/assays/'

	def form_valid(self, form):
		form.instance.updated_by = self.request.user
		return super().form_valid(self.request.user,form)

class AssaysDeleteView(DeleteView):
	model = Assay
	template_name = 'assays/delete_assay.html'
	success_url = reverse_lazy('assays')

'''def assay_delete(request, assay_id):
	assay = Assay.objects.get(pk=int(assay_id))
	print(assay)
	#assay.delete()
	return redirect('assays')
'''
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
			25: self.get_object().iinflc05s.annotate(),
			26: self.get_object().iinflc06s.annotate(),	
			27: self.get_object().fc07s.annotate(),
			28: self.get_object().pr02s.annotate(),
			29: self.get_object().cba01s.annotate(),								
			30: self.get_object().cba02s.annotate(),
			31: self.get_object().hpibd03s.annotate(),
			32: self.get_object().hpibd01s.annotate(),
			33: self.get_object().hpibd04s.annotate(),
			34: self.get_object().endo01s.annotate(),
			35: self.get_object().iinflc01s.annotate(),
			36: self.get_object().ar03s.annotate(),
			37: self.get_object().ar04s.annotate(),
			38: self.get_object().ar05s.annotate(),
			39: self.get_object().ar06s.annotate(),
		}
		# mouselist = i4.values('mid').distinct().order_by('mid')
		# objects = Mouse.objects.filter(id__in=mouselist)
		#images = self.get_object().associated_images.annotate()
		par = None
		if(	self.request.GET.get('parameterName')):
			par = self.request.GET.get('parameterName')
		#	kwargs['par']=request.POST.get('parameterName')
		measures = switcher.get(self.object.type.id,"Ivalid")
		kwargs['measures'] = measures
		parameters = get_parameters(self.object)
		mouselist = measures.values('mid').distinct().order_by('mid')
		mouse_num = measures.values('mid').annotate(dcount=Count('mid')).count()	
		females = 	Mouse.objects.filter(id__in=mouselist).filter(gender='Female')
		males = 	Mouse.objects.filter(id__in=mouselist).filter(gender='Male')
		kwargs['mouselist'] = Mouse.objects.filter(id__in=mouselist)
		kwargs['total'] = mouse_num
		kwargs['assayjson']= json.dumps(self.object.id)
		kwargs['females'] = females.count()
		kwargs['males'] = males.count()
		kwargs['parameters'] = parameters
		kwargs['par'] = par
		source = parameters[0]
		if par:
			source = par
		test = parameterMeasures(measures,parameters[0])
		series = []
		for key in test:
			data_dict = {}
			data_dict['name'] = key
			data_dict['data'] = test[key].values.tolist()
			print(data_dict)
			series.append(data_dict)
		kwargs['scarplot'] = [[161.2, 51.6], [167.5, 59.0], [159.5, 49.2], [157.0, 63.0], [155.8, 53.6], [170.0, 59.0], [159.1, 47.6], [166.0, 69.8], [176.2, 66.8], [160.2, 75.2]]
		'''series = [{
		'name': 'Female',
		'color': '#343a40',
		'data': [[161.2, 51.6], [167.5, 59.0], [159.5, 49.2], [157.0, 63.0], [155.8, 53.6], [170.0, 59.0], [159.1, 47.6], [166.0, 69.8], [176.2, 66.8], [160.2, 75.2]]
		},
		{
		'name': 'Female WT',
		'data': [[167.6, 58.3], [165.1, 56.2], [160.0, 50.2], [170.0, 72.9], [157.5, 59.8],
		[167.6, 61.0], [160.7, 69.1], [163.2, 55.9], [152.4, 46.5], [157.5, 54.3],
		[168.3, 54.8], [180.3, 60.7], [165.5, 60.0], [165.0, 62.0], [164.5, 60.3]]
		}
		]'''
		kwargs['series'] = series
		return super().get_context_data(**kwargs)

def returnMeasurements(assay):
	measures = 0
	switcher ={
		4: assay.iinflc03s.annotate(),
		5: assay.iinflc04s.annotate(),
		6: assay.iinflc02s.annotate(),
		7: assay.ni01s.annotate(),
		8: assay.ni02rot01s.annotate(),
		9: assay.ni02ofd01s.annotate(),
		10: assay.ni02grs01s.annotate(),
		11: assay.hem01s.annotate(),
		12: assay.hpibd02s.annotate(),
		13: assay.biochem01s.annotate(),
		14: assay.biochem02s.annotate(),
		15: assay.biochem03s.annotate(),
		16: assay.biochem04s.annotate(),
		17: assay.biochem05s.annotate(),
		18: assay.biochem06s.annotate(),
		19: assay.biochem07s.annotate(),
		20: assay.biochem08s.annotate(),
		22: assay.hpni01s.annotate(),
		23: assay.fc08s.annotate(),
		24: assay.ar02s.annotate(),
		25: assay.iinflc05s.annotate(),
		26: assay.iinflc06s.annotate(),	
		27: assay.fc07s.annotate(),
		28: assay.pr02s.annotate(),
		29: assay.cba01s.annotate(),								
		30: assay.cba02s.annotate(),
		31: assay.hpibd03s.annotate(),
		32: assay.hpibd01s.annotate(),
		33: assay.hpibd04s.annotate(),
		34: assay.endo01s.annotate(),
		35: assay.iinflc01s.annotate(),
		36: assay.ar03s.annotate(),
		37: assay.ar04s.annotate(),
		38: assay.ar05s.annotate(),
		39: assay.ar06s.annotate(),
	}
	measures = switcher.get(assay.type.id,"Ivalid")
	return measures

def selectParameters(request):
	par=request.POST.get('parameterName')
	print(par)
	return redirect(request.META['HTTP_REFERER'],{'par': par})

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
		user = get_object_or_404(User,username=self.kwargs.get('username'))
		kwargs['flag'] = 1
		a= Assay.objects.filter(author=user).order_by('measurement_day')
		#a_measurements = []
		#for assay in a:
		#	measures = switcher.get(assay.object.type.id,"Ivalid")
		#	a_measurements.append(len(measures))
		b= Assay.objects.filter(scientist=user).order_by('measurement_day')	
		kwargs['access_assays'] = Assay.objects.filter(scientist=user).order_by('measurement_day')
		kwargs['user_assays'] = Assay.objects.filter(author=user).order_by('measurement_day')
		kwargs['all'] = len(a) + len(b)
		kwargs['a'] = len(a)
		kwargs['b'] = len(b)
		#kwargs['a_measurements'] = a_measurements
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

class FacilityAssaysListView(LoginRequiredMixin,ListView):
	model = Assay
	template_name = 'assays/user-assays.html'
	context_object_name = 'list_assays'

	def get_queryset(self):
		user = get_object_or_404(User,username=self.kwargs.get('username'))
		atypes = Atype.objects.filter(facilitylong__id=user.profile.facility.id)
		return Assay.objects.filter(type__in=atypes).order_by('measurement_day')

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
'''def piecharts(request):
	labels = []
	data = []
	assay = Assay.objects
	queryset = 
'''
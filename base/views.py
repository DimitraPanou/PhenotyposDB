from django.shortcuts import render, redirect,get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
    TemplateView
)
from django.urls import reverse_lazy
#from .forms import AssayForm
from .models import Book
from assays.models import Assay, Mouse
from pipelines.models import Pipeline
# Create your views here.
from django.db.models import Q

from django.conf import settings
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.contrib.staticfiles import finders

@login_required(login_url ='login')
def home_view(request, *args, **kargs):
	#return HttpResponse("<h1>Home</h1>")
	return render(request, "home.html")
    #return redirect('profile')

def chart_view(request, *args, **kargs):
	#return HttpResponse("<h1>Home</h1>")
	return render(request, "chart.html")


def search_view(request, *args, **kargs):
    #return HttpResponse("<h1>Home</h1>")
    if request.method == 'POST':
        searched = request.POST['searched']
        print(searched)
        assays = Assay.objects.filter(Q(name__contains = searched) | Q(type__facilitylong__name__contains=searched))
        pipelines = Pipeline.objects.filter(name__contains = searched)
        return render(request, "search.html",{'searched':searched,
        'assays': assays,
        'pipelines': pipelines})
    else:
        return render(request, "search.html")

def upload(request):
	context = {}
	if request.method == 'POST':
		upload_file = request.FILES['document']
		fs = FileSystemStorage()
		name = fs.save(upload_file.name,upload_file)
		url = fs.url(name)
		context['url'] = url
	return render(request, 'upload.html',context)


def books(request, *args, **kargs):
	books = Book.objects.all()
	print(books)
	return render(request,'books.html',{'books': books})

def add_book(request, *args, **kargs):
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('books')
    else:
        form = BookForm()
    return render(request, 'add_book.html', {
        'form': form
    })

def link_callback(uri, rel):
    result = finders.find(uri)
    if result:
        if not isinstance(result, (list, tuple)):
            result = [result]
        result = list(os.path.realpath(path) for path in result)
        path=result[0]
    else:
        sUrl = settings.STATIC_URL        # Typically /static/
        sRoot = settings.STATIC_ROOT      # Typically /home/userX/project_static/
        mUrl = settings.MEDIA_URL         # Typically /media/
        mRoot = settings.MEDIA_ROOT       # Typically /home/userX/project_static/media/
        if uri.startswith(mUrl):
            path = os.path.join(mRoot, uri.replace(mUrl, ""))
        elif uri.startswith(sUrl):
            path = os.path.join(sRoot, uri.replace(sUrl, ""))
        else:
            return uri
            # make sure that file exists
    if not os.path.isfile(path):
        raise Exception(
            'media URI must start with %s or %s' % (sUrl, mUrl)
        )
    return path

def get_context(assay):
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
        40: assay.ar07s.annotate(),
        41: assay.cba03s.annotate(),
        42: assay.fc01s.annotate(),
        43: assay.fc03s.annotate(),
        44: assay.hpa02s.annotate(),
        45: assay.fc04s.annotate()
    }
    measures = switcher.get(assay.type.id,"Ivalid")
    return measures

def render_pdf_view(request, pk):
    template_path = 'user_printer.html'
    print(str(pk))
    assaymodel = Assay.objects.get(id=pk)
    measures = get_context(assaymodel)
    print(measures)
    assayname="report"+str(pk)+".pdf"
    context = {'myvar': 'this is your template context','assay': assaymodel,'measures': measures}
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="%s"' %assayname
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)
    # create a pdf
    pisa_status = pisa.CreatePDF(
       html, dest=response, link_callback=link_callback)
    # if error then show some funy view
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response
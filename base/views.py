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

def render_pdf_view(request, pk):
    template_path = 'user_printer.html'
    print(str(pk))
    assayname="report"+str(pk)+".pdf"
    context = {'myvar': 'this is your template context'}
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



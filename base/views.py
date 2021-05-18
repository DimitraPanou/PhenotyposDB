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
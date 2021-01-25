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

# Create your views here.

@login_required(login_url ='login')
def home_view(request, *args, **kargs):
	#return HttpResponse("<h1>Home</h1>")
	return render(request, "home.html")


def chart_view(request, *args, **kargs):
	#return HttpResponse("<h1>Home</h1>")
	return render(request, "chart.html")


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
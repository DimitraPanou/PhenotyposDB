from django.http import HttpResponse
from django.shortcuts import redirect
from django.shortcuts import render, redirect,get_object_or_404

def unauthenticated_user(view_func):
	def wrapper_func(request, *args, **kwargs):
		if(request.user.is_authenticated):
			return redirect('home')
		else:
			return view_func(request, *args, **kwargs)
	return wrapper_func


def admin_only(view_func):
	def wrapper_function(request, *args, **kwargs):
		group = None
		if request.user.groups.exists():
			group = request.user.groups.all()[0].name

		if group == 'admin':
			return view_func(request, *args, **kwargs)
		else:
			print("No permission here")
			return HttpResponse("No permission")
	return wrapper_function

def allowed_users(allowed_roles=[]):
	def decorator(view_func):
		def wrapper_func(request, *args, **kwargs):

			group = None
			if request.user.groups.exists():
				group = request.user.groups.all()[0].name

			if group in allowed_roles:
				return view_func(request, *args, **kwargs)
			else:
				return render(request, "error404.html")
				#return HttpResponse('You are not authorized to view this page')
		return wrapper_func
	return decorator
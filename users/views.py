from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .decorators import allowed_users
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm, UserProfileUpdateForm
from .models import Profile
from django.contrib.auth.models import User
from django.db import IntegrityError, transaction

from .decorators import unauthenticated_user

@unauthenticated_user
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, 'Your account has been created! You are now able to log in')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


@login_required
@transaction.atomic
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, 'Your account has been updated!')
            return redirect('profile')
        else:
            messages.error(request,'Please correct the error below.')    

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'users/profile.html', context)

@allowed_users(allowed_roles=['Admin'])
def editUser(request,pk):
    user1 = User.objects.get(id=pk)
    print(user1, user1.id, user1.profile, pk)
    u_form = UserUpdateForm(instance=user1)
    p_form = UserProfileUpdateForm(instance=user1.profile)
    if request.method == 'POST':
        u_form = UserUpdateForm(instance=user1)    
        p_form = UserProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=user1.profile)
        if u_form.is_valid() and p_form.is_valid():
            messages.success(request, 'Your account has been updated!')
            u_form.save()
            p_form.save()
            return redirect('edit-user',pk=pk)
        else:
            messages.error(request,'Please correct the error below.')    
    context = {
        'user1': user1,
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request, 'users/edit-profile.html', context)

@allowed_users(allowed_roles=['Admin'])
def users_all(request):
    users = Profile.objects.all()
    flag_users =1
    #for 
    #groups = User.objects.groups.all()
    return render(request, 'users/users_all.html', {
        'users': users,
        'flag_users':flag_users
    })

@login_required
#@transaction.atomic
def test(request):

    u_form = UserUpdateForm(instance=request.user)
    p_form = ProfileUpdateForm(instance=request.user.profile)
    print(u_form)
    print(p_form)
    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'users/test.html', context)
#class Profile(DetailView):
#	template_name='users/profile.html'
#	queryset = User.objects.all()

#	def get_object(self):
#		id_ = self.kwargs.get()

#ALTER USER postgres PASSWORD 'dim123!@#';
#CREATE ROLE DK_LAB LOGIN SUPERUSER PASSWORD 'DKontogiann1s';
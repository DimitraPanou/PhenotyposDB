"""fleming URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static

from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include

from base.views import *
from assays.views import *
from users.views import *

from pipelines.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home_view, name='home'),
    path('chart',chart_view, name='chart'),
    #Assays
    #path('assays/', include('assays.urls', namespace="assays")),
    ###########
	#  Assays #
	###########
	path('assays/',assayslist,name='assays'),
	path('assays/<str:username>',UserAssaysListView.as_view(),name='user-assays'),
	path('assays/<str:username>/access',GroupAssaysListView.as_view(),name='group-assays'),
	path('assays/<str:username>/lab',FacilityAssaysListView.as_view(),name='lab-assays'),

	path('assays/add/',add_assay,name='add_assay'),
#
#	path('assays/add/',AssaysCreateView.as_view(),name='add_assay'),
	path('assays/update/<int:pk>/', AssaysUpdateView.as_view(), name='assay-update'),
	path('assays/<int:pk>/', AssaysDetailView.as_view(), name='assay-detail'),
	path('assays/charts/<int:pk>/', AssaysDetailView2.as_view(), name='assay-detail2'),
	#path('assays/<int:pk>/', AssaysUpdateView.as_view(), name='assay-update'),
#
	#path('assays/delete/<int:pk>/', assay_delete, name='assay_delete'),
	path('assays/<int:pk>/delete/', AssaysDeleteView.as_view(), name='assay-delete'),
	#path('assays/<int:pk>/delete/', assay_delete, name='assay-delete'),
#
	path('assays/types/',AtypeListView.as_view(),name='atypes'),
#
	path('assays/types/<int:pk>/', AtypeDetailView.as_view(), name='assaytype-detail'),
#
	path('assays/types/edit/<int:pk>/', Atype2UpdateView.as_view(), name='assaytype-detail-update'),
#
	path('assays/types/add',add_atype,name='add_atype'),
#
	path('assays/types/update/<int:pk>/', AtypeUpdateView.as_view(), name='assaytype-update'),
#
	path('assays/types/<int:pk>/delete/', AtypeDeleteView.as_view(), name='assaytype-delete'),
	path('assays/<int:pk>/addimages', uploadImage, name='uploadImage'),

	#path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),

##########################################
##             pipelines                ##
#########################################
	path('pipelines/',pipelineslist,name='pipelines'),
	path('pipelines/add/',add_pipeline,name='add-pipeline'),
	path('pipelines/update/<int:pk>/', PipelineUpdateView.as_view(), name='pipeline-update'),
	path('pipelines2/<int:pk>/', pipeline_detail_view, name='pipeline-detail2'),
	path('pipelines/<int:pk>/', PipelineDetailView.as_view(), name='pipeline-detail'),
	path('pipelines/<int:pk>/delete/', PipelineDeleteView.as_view(), name='pipeline-delete'),
	path('pipelines/<str:username>',UserPipelineListView.as_view(),name='user-pipelines'),	
	path('pipelines/types/',PipelineTypeListView.as_view(),name='pipelinetypes'),
	path('pipelines/<int:pk>/add/new', add_assay_to_pipeline, name='add_assay_to_pipeline'),

	#path('pipelines/types/<int:pk>/', PipelineTypeDetailView.as_view(), name='pipelinetype-detail'),
	path('pipelines/types/add',add_pipelinetype,name='add_pipelinetype'),
	path('pipelines/types/update/<int:pk>/', PipelineTypeUpdateView.as_view(), name='pipelinetype-update'),
	path('pipelines/types/<int:pk>/delete/', PipelineTypeDeleteView.as_view(), name='pipelinetype-delete'),

	####################################	
	#User
	####################################
	path('register', register, name='register'),
	path('userprofile', profile, name='profile'),
	#path('profile', profile, name='profile'),
	path('test', test, name='test'),
	path('login', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
	path('logout', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
	path('password-reset/', auth_views.PasswordResetView.as_view(template_name='users/password_reset.html'), name='password_reset'),
	path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'), name='password_reset_done'),
	path('password-reset-confirm/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'), name='password_reset_confirm'),
	path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'), name='password_reset_complete'),
	path('users', users_all, name='users_all'),
	path('search', search_view, name='search'),
	path('selectParameters', selectParameters, name='selectParameters'),

	#path('piecharts/', piecharts, name='piecharts'),
]

''''
	#Mouse
	path('mice',AssaysListView.as_view(),name='assays'),
	path('mice/add/',add_assay,name='add_assay'),
	path('mice/update/<int:pk>/', AssaysUpdateView.as_view(), name='assay-update'),
	path('assays/<int:pk>/delete/', AssaysDeleteView.as_view(), name='assay-delete'),
'''
'''
	#Pipelines
	path('pipelines/',PipelinesListView.as_view(),name='pipelines'),
	path('pipelines/add/',add_pipeline,name='add_pipeline'),
	path('pipelines/update/<int:pk>/', PipelinesUpdateView.as_view(), name='pipeline-update'),
    #path('pipelines/<int:pk>/delete/', PipelinesDeleteView.as_view(), name='pipeline-delete'),

	path('test',test_view, name='test'),
		#Infopages
	path('pipelines/info/',pipeline_info_view,name='pipelines_info'),
	path('pipelines/info/GIP-1/',gip1_view,name='gip1'),
'''

if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root= settings.STATIC_ROOT)
	urlpatterns += static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
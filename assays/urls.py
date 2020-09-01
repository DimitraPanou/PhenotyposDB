from django.urls import path
#from .views import (
#    product_create_view, 
#    product_detail_view, 
#    product_delete_view,
#    product_list_view,
#    product_update_view,   
#)
from .views import (
    AssaysListView,
    AssaysUpdateView,
    AssaysCreateView,
    AssaysDeleteView,
    AssaysDetailView,
    AtypeListView,
    AtypeUpdateView,
    AtypeDeleteView,
    AtypeDetailView,
    Atype2UpdateView,
    add_atype    
)

app_name = 'assays'

urlpatterns = [
    path('', AssaysListView.as_view(),name='assays'),
    path('add/', AssaysCreateView.as_view(), name='add_assay'),
    path('<int:id>/', AssaysDetailView.as_view(), name='assay-detail'),
    path('update/<int:id>/', AssaysUpdateView.as_view(), name='assay-update'),
    path('<int:id>/delete/', AssaysDeleteView.as_view(), name='assay-delete'),
    path('types/',AtypeListView.as_view(),name='atypes'),
    path('types/<int:id>/', AtypeDetailView.as_view(), name='assaytype-detail'),
    path('types/<int:id>/edit', Atype2UpdateView.as_view(), name='assaytype-detail-update'),
    path('types/add',add_atype,name='add_atype'),
    path('types/update/<int:id>/', AtypeUpdateView.as_view(), name='assaytype-update'),
    path('types/<int:id>/delete/', AtypeDeleteView.as_view(), name='assaytype-delete'),
]
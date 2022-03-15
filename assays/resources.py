from import_export import resources
from .models import *

class AtypeResource(resources.ModelResource):
    class Meta:
    	model = Atype

class AssayResource(resources.ModelResource):
    class Meta:
    	model = Assay

class FacilityResource(resources.ModelResource):
    class Meta:
    	model = Facility
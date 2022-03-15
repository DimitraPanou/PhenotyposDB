
# Register your models here.
from django.contrib import admin

# Register your models here.
from .models import *
from import_export.admin import ImportExportModelAdmin


@admin.register(Atype)
class AtypeAdmin(ImportExportModelAdmin):
	list_display = ('code', 'name', 'facilitylong','service_type','staff','publication_date','version')
	pass

class ImageInline(admin.TabularInline):
    model = AssociatedImage

@admin.register(Assay)
class AssayAdmin(ImportExportModelAdmin):
	fields = ['code','name','type','version','staff','measurement_day','scientist_in_charge','members','assayqc','rawdata_file','comments']
	list_display = ('code','name','type','version','staff','measurement_day','scientist_in_charge','get_members','assayqc','rawdata_file','comments')
	inlines = [
        ImageInline
    ]
	pass

@admin.register(Facility)
class FacilityAdmin(ImportExportModelAdmin):
	list_display = ('name', 'details')
	pass


#admin.site.register(Book)
admin.site.register(Iinflc04)
admin.site.register(Ni02Rot01)
admin.site.register(Ni02grs01)
admin.site.register(Ni02ofd01)
admin.site.register(Ni01)
admin.site.register(Fc04)
#admin.site.register(Atype)
#admin.site.register(Assay)
admin.site.register(Mouse)
admin.site.register(AssociatedImage)

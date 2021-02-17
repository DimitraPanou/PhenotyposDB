
# Register your models here.
from django.contrib import admin

# Register your models here.
from .models import *
from import_export.admin import ImportExportModelAdmin

@admin.register(Atype)
class AtypeAdmin(ImportExportModelAdmin):
	list_display = ('code', 'name', 'facility','unit','staff','publication_date','version')
	pass

@admin.register(Assay)
class AssayAdmin(ImportExportModelAdmin):
	list_display = ('code', 'name','type','version','staff','measurement_day','scientist','assayqc','rawdata_file','comments')
	pass

#admin.site.register(Book)
admin.site.register(Iinflc04)
admin.site.register(Ni02Rot01)
admin.site.register(Ni02grs01)
admin.site.register(Ni02ofd01)
admin.site.register(Ni01)
admin.site.register(Facility)
#admin.site.register(Atype)
#admin.site.register(Assay)
admin.site.register(Mouse)
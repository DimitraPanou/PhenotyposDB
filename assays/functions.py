from .models import *
import openpyxl
from openpyxl import Workbook
import collections

from django.shortcuts import get_object_or_404
from datetime import date
tableNames = ['BIOCHEM-01','BIOCHEM-02','BIOCHEM-03','BIOCHEM-04','BIOCHEM-05',
				'BIOCHEM-06','BIOCHEM-07','BIOCHEM-08','CBA-01','CBA-02','ENDO-01','FC-04',
				'FC-07','HEM-01','HPIBD-01','HPIBD-02','HPIBD-03','HPNI-01','IINFLC-01',
				'IINFLC-02','IINFLC-03','IINFLC-04','NI-01','NI-02-GRS-01','NI-02-OFD-01',
				'NI-02-ROT-01','PR-02',"info"
				]



def create_mouseHash(data):
	for i in range(len(data["Mouse ID"])):
		m = Mouse()
		#print("MOUSE")
		for key in data:
			if ('ID' in key):
				m.mid = data[key][i]			
			elif ('genotype' in key.lower()):
				m.genotype = data[key][i]
			elif ('strain' in key.lower()):
				m.strain = data[key][i]
			elif ('tail' in key.lower()):
				m.tail_num = data[key][i]				 
			elif ('induced' in key.lower()):
				m.induced = data[key][i]
			elif ('treated' in key.lower() or 'treatement' in key.lower()):
				m.treated = data[key][i]
			elif ('gender' in key.lower() or 'sex' in key.lower()):
				m.gender = data[key][i] 
			elif ('Age' in key):
				m.age = data[key][i] 
			elif ('birth' in key.lower()):
				m.dateofBirth = data[key][i] 				
			elif ('diet' in key.lower()):
				m.diet = data[key][i] 
			elif ('cage' in key.lower()):
				m.mouse_info = data[key][i]
			elif ('environmental' in key.lower()):
				m.other = data[key][i]
			elif ('report' in key.lower()):
				m.health_report = data[key][i]
		if(Mouse.objects.filter(mid=m.mid, genotype=m.genotype,dateofBirth=m.dateofBirth)):
			continue;
		print("Saving mouse {}".format(m.mid)) 	
		m.save()

def data_iinflc04(data,assay):
	for i in range(len(data["Mouse ID"])):
		flag =1
		iinflc04 = Iinflc04()
		iinflc04.assayid = assay
		for key in data:
			if(flag):
				if ('ID' in key):
					#Return mouse id from mouse table
					#print(data[key][i])
					mouse = Mouse.objects.get(mid=data[key][i])
					if(mouse): 
						iinflc04.mid = mouse
					else:
						flag = 0
						break;			
				elif ('timepoint' in key.lower()):
					iinflc04.timepoint= int(data[key][i])
				elif ('age' in key.lower()):
					iinflc04.age= data[key][i]
				elif ('measurement' in key.lower()):
					d = data[key][i]
					iinflc04.measurement_date= d				 
				elif ('weight' in key.lower()):
					iinflc04.weight= data[key][i]
				elif ('comment' in key.lower()):
					iinflc04.comment= data[key][i]				
		iinflc04.save()


def data_ni01(data,assay):
	for i in range(len(data["Mouse ID"])):
		flag =1
		ni01 = Ni01()
		ni01.assayid = assay
		for key in data:
			if(flag):
				if ('ID' in key):
					#Return mouse id from mouse table
					#print(data[key][i])
					mouse = Mouse.objects.get(mid=data[key][i])
					if(mouse): 
						ni01.mid = mouse
					else:
						flag = 0
						break;			
				elif ('timepoint' in key.lower()):
					ni01.timepoint= int(data[key][i])
				elif ('age' in key.lower()):
					ni01.age= data[key][i]
				elif ('measurement' in key.lower()):
					d = data[key][i]
					ni01.measurement_date= d				 
				elif ('clinical' in key.lower()):
					ni01.clinical_score= data[key][i]
				elif ('comment' in key.lower()):
					ni01.comment= data[key][i]				
		ni01.save()

def data_ni02rot01(data,assay):
	for i in range(len(data["Mouse ID"])):
		flag =1
		experiment = Ni02Rot01()
		experiment.assayid = assay
		for key in data:
			if(flag):
				if ('ID' in key):
					#Return mouse id from mouse table
					#print(data[key][i])
					mouse = Mouse.objects.get(mid=data[key][i])
					if(mouse): 
						experiment.mid = mouse
					else:
						flag = 0
						break;			
				elif ('timepoint' in key.lower()):
					experiment.timepoint= int(data[key][i])
				elif ('age' in key.lower()):
					experiment.age= data[key][i]
				elif ('measurement' in key.lower()):
					d = data[key][i]
					experiment.measurement_date= d				 
				elif ('individual latency' in key.lower()):
					if('1' in key.lower()):
						experiment.individual_latency_fall1 = data[key][i]
					else:
						experiment.individual_latency_fall2 = data[key][i]
				elif ('speed' in key.lower()):
					if('1' in key.lower()):
						experiment.speed_fall1 = data[key][i]
					else:
						experiment.speed_fall2 = data[key][i]
				elif ('mean latency' in key.lower()):
					experiment.mean_latency_fall= data[key][i]
				elif ('comment' in key.lower()):
					experiment.comment= data[key][i]				
		experiment.save()

def data_ni02ofd01(data,assay):
	for i in range(len(data["Mouse ID"])):
		flag =1
		experiment = Ni02ofd01()
		experiment.assayid = assay
		for key in data:
			if(flag):
				if ('ID' in key):
					#Return mouse id from mouse table
					#print(data[key][i])
					mouse = Mouse.objects.get(mid=data[key][i])
					if(mouse): 
						experiment.mid = mouse
					else:
						flag = 0
						break;			
				elif ('timepoint' in key.lower()):
					experiment.timepoint= int(data[key][i])
				elif ('measurement' in key.lower()):
					d = data[key][i]
					experiment.measurement_date= d				 
				elif ('comment' in key.lower()):
					experiment.comment= data[key][i]
				elif ('Age' in key):
					print('strain: ',data[key][i])
					experiment.age= data[key][i]
				elif ('distance' in key.lower()):
					if('arena' in key.lower()):
						print('age',data[key][i])						
						experiment.total_distance_wa = data[key][i]
					elif('peripheral' in key.lower()): 
						experiment.total_distance_pz = data[key][i]
					elif('central' in key.lower()):
						experiment.total_distance_cz = data[key][i]
				elif ('time spent' in key.lower()):
					if('peripheral' in key.lower()):
						experiment.time_pz = data[key][i]
					elif('central' in key.lower()):
						experiment.time_cz = data[key][i]
				elif ('speed' in key.lower()):
					if('arena' in key.lower()):
						experiment.avg_speed_wa = data[key][i]
					elif('peripheral' in key.lower()): 
						experiment.avg_speed_pz = data[key][i]
					elif('central' in key.lower()):
						experiment.avg_speed_cz = data[key][i]
		experiment.save()

def data_ni02grs01(data,assay):
	for i in range(len(data["Mouse ID"])):
		flag =1
		experiment = Ni02grs01()
		experiment.assayid = assay
		for key in data:
			if(flag):
				if ('ID' in key):
					#Return mouse id from mouse table
					#print(data[key][i])
					mouse = Mouse.objects.get(mid=data[key][i])
					if(mouse): 
						experiment.mid = mouse
					else:
						flag = 0
						break;			
				elif ('timepoint' in key.lower()):
					experiment.timepoint= int(data[key][i])
				elif ('measurement date' in key.lower()):
					d = data[key][i]
					experiment.measurement_date= d
				elif ('Age' in key):
					experiment.age= data[key][i]
				elif ('body weight (g)' in key.lower()):
					experiment.weight= data[key][i]
				elif ('comment' in key.lower()):
					experiment.comment= data[key][i]
				elif ('forelimb grip' in key.lower()):
					#print('forelimb grip: ',data[key][i])
					if('measurement 1' in key.lower()):
						experiment.forelimb_r1 = data[key][i]
					elif('measurement 2' in key.lower()):
						experiment.forelimb_r2 = data[key][i]
					elif('measurement 3' in key.lower()):
						experiment.forelimb_r3 = data[key][i]
					elif('measurement mean' in key.lower()):
						#print('pass 4: ',data[key][i])						
						experiment.forelimb = data[key][i]
					elif('ratio' in key.lower()):
						experiment.forelimb_mean_ratio = data[key][i]
				elif ('hindlimb' in key.lower()):
					if('measurement 1' in key.lower()):
						experiment.hindlimb_r1 = data[key][i]
					elif('measurement 2' in key.lower()): 
						experiment.hindlimb_r2 = data[key][i]
					elif('measurement 3' in key.lower()):
						experiment.hindlimb_r3 = data[key][i]
					elif('measurement mean' in key.lower()):
						experiment.hindlimb = data[key][i]
					elif('ratio' in key.lower()):
						#print('pass 5: ',data[key][i])
						experiment.hindlimb_mean_ratio = data[key][i]		
		experiment.save()

def data_hem01(data,assay):
	for i in range(len(data["Mouse ID"])):
		flag =1
		experiment = Hem01()
		experiment.assayid = assay
		for key in data:
			if(flag):
				if ('Mouse ID' == key):
					#Return mouse id from mouse table
					#print(data[key][i])
					mouse = Mouse.objects.get(mid=data[key][i])
					if(mouse): 
						experiment.mid = mouse
					else:
						flag = 0
						break;			
				elif ('timepoint' in key.lower()):
					experiment.timepoint= int(data[key][i])
				elif ('measurement date' in key.lower()):
					d = data[key][i]
					experiment.measurement_date= d
				elif ('Age' in key):
					experiment.age= data[key][i]
				elif ('comment' in key.lower()):
					experiment.comment= data[key][i]
				elif ('sample id' in key.lower()):
					experiment.sample_id= data[key][i]
				elif ('wbc count' in key.lower()):
					experiment.wbc_count= data[key][i]		
				elif ('# mononuclear cells' in key.lower()):
					experiment.mononuclear_num= data[key][i]
				elif ('# lymphocytes' in key.lower()):
					experiment.lymphocytes_num= data[key][i]
				elif ('% lymphocytes' in key.lower()):
					experiment.lymphocytes_per= data[key][i]
				elif ('# monocytes' in key.lower()):
					if('2' in key.lower()):
						experiment.monocytes2_num= data[key][i]
					else:
						experiment.monocytes_num= data[key][i]
				elif ('# neutrophils' in key.lower()):
					experiment.neutrophils_num= data[key][i]
				elif ('% neutrophils' in key.lower()):
					experiment.neutrophils_per= data[key][i]
				elif ('# eosinophils' in key.lower()):
					experiment.eosinophils_num= data[key][i]
				elif ('% eosinophils' in key.lower()):
					experiment.eosinophils_per= data[key][i]
				elif ('# basophils' in key.lower()):
					experiment.basophils_num= data[key][i]
				elif ('% basophils' in key.lower()):
					experiment.basophils_per= data[key][i]
				elif ('rbc count' in key.lower()):
					experiment.rbc_count= data[key][i]
				elif ('hematocrit' in key.lower()):
					experiment.ht= data[key][i]
				elif ('hemoblobin' in key.lower()):
					experiment.hb= data[key][i]
				elif ('plt platelet' in key.lower()):
					experiment.plt_count= data[key][i]
				elif ('platelet dist' in key.lower()):
					experiment.platelet_dist_range= data[key][i]
				elif ('platelet count' in key.lower()):
					experiment.platelet_count= data[key][i]
				elif ('average volume' in key.lower()):
					experiment.avg_vol_platelets= data[key][i]
				elif ('MCV' == key):
					experiment.mcv= data[key][i]
				elif ('RDV' == key):
					experiment.rdv= data[key][i]
				elif ('MCHC' == key):
					experiment.mchc= data[key][i]	
				elif ('MCV2' == key):
					experiment.mcv2= data[key][i]					
		experiment.save()


#Returns number of rows & number of columns with data in excel tab  
def find_edges(sheet):
    row = sheet.max_row
    while row > 0:
        cells = sheet[row]
        if all([cell.value is None for cell in cells]):
            row -= 1
        else:
            break
    if row == 0:
        return 0, 0

    column = sheet.max_column
    while column > 0:
        cells = next(sheet.iter_cols(min_col=column, max_col=column, max_row=row))
        if all([cell.value is None for cell in cells]):
            column -= 1
        else:
            break
    return row, column

def dataofAssay(assay,filename):
	wb = openpyxl.load_workbook(filename, data_only=True)
	print("OK")
	#Optional condition
	if(assay not in tableNames):
		print(assay)
		return -1;
	#For info tab to find the mouselist
	if(assay in "info"):
		sheet = wb[wb.sheetnames[0]]
	#For regular assay
	else:
		sheet = wb[assay]
	[rows,cols]=find_edges(sheet)
	d = {}
	d = collections.OrderedDict()

	# If mouseID // mouse strain
	for c in range(1,cols):
		r0 = sheet.cell(row=1, column = c).value
		if(r0 and r0 not in d):
			d[r0] = []
		for r in range(2,rows+1):
			object = sheet.cell(row=r, column = c).value
			d[r0].append(object)
	return d;

def handle_uploaded_file(assayobject):
    #with open('some/file/name.txt', 'wb+') as destination:
    #    for chunk in f.chunks():
    #        destination.write(chunk)
	fname = '../static'+assayobject.rawdata_file.url
	wb = openpyxl.load_workbook(fname)
	info = dataofAssay("info",fname)
	#print(info)
	data = dataofAssay(assayobject.type.code,fname)
	print(data.keys())
	print("Data")
	print(data)
	#print(len(data["Mouse ID"]))
	create_mouseHash(info)
	if(assayobject.type.code == "IINFLC-04"):
		data_iinflc04(data,assayobject)
	if(assayobject.type.code == "NI-01"):
		data_ni01(data,assayobject)
	if(assayobject.type.code == "NI-02-ROT-01"):
		data_ni02rot01(data,assayobject)
	if(assayobject.type.code == "NI-02-OFD-01"):
		data_ni02ofd01(data,assayobject)
	if(assayobject.type.code == "NI-02-GRS-01"):
		data_ni02grs01(data,assayobject)
	if(assayobject.type.code == "HEM-01"):
		data_hem01(data,assayobject)

def returnTemplateName(assayobject):
	switcher ={
		5:'assays/assaytypes/iinflc-04.html',
		7:'assays/assaytypes/ni01.html',
		8:'assays/assaytypes/ni02rot01.html',
		9:'assays/assaytypes/ni02ofd01.html'
	}
	return switcher.get(assayobject.id,"Ivalid")
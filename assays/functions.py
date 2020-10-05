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
				#print('mouseID: ',data[key][i])
				m.mid = data[key][i]			
			elif ('genotype' in key.lower()):
				#print('genotype: ',data[key][i])
				m.genotype = data[key][i]
			elif ('strain' in key.lower()):
				#print('strain: ',data[key][i])
				m.strain = data[key][i]
			elif ('tail' in key.lower()):
				#print('tail_num: ',data[key][i])
				m.tail_num = data[key][i]				 
			elif ('induced' in key.lower()):
				#print('induced: ',data[key][i])
				m.induced = data[key][i]
			elif ('treated' in key.lower() or 'treatement' in key.lower()):
				#print('treated: ',data[key][i])
				m.treated = data[key][i]
			elif ('gender' in key.lower() or 'sex' in key.lower()):
				#print('gender: ',data[key][i])
				m.gender = data[key][i] 
			elif ('Age' in key):
				#print('age: ',data[key][i])
				m.age = data[key][i] 
			elif ('birth' in key.lower()):
				#print('date of birth: ',data[key][i])
				m.dateofBirth = data[key][i] 				
			elif ('diet' in key.lower()):
				#print('diet: ',data[key][i])
				m.diet = data[key][i] 
			elif ('cage' in key.lower()):
				#print('other cage: ',data[key][i]) 
				m.mouse_info = data[key][i]
			elif ('environmental' in key.lower()):
				#print('other env: ',data[key][i]) 
				m.other = data[key][i]
			elif ('report' in key.lower()):
				#print('health_report: ',data[key][i]) 
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
					#print('genotype: ',data[key][i])
					iinflc04.timepoint= int(data[key][i])
				elif ('age' in key.lower()):
					#print('strain: ',data[key][i])
					iinflc04.age= data[key][i]
				elif ('measurement' in key.lower()):
					print(data[key][i])
					d = data[key][i]
					iinflc04.measurement_date= d				 
				elif ('weight' in key.lower()):
					#print('induced: ',data[key][i])
					iinflc04.weight= data[key][i]
				elif ('comment' in key.lower()):
					#print('induced: ',data[key][i])
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
					#print('genotype: ',data[key][i])
					ni01.timepoint= int(data[key][i])
				elif ('age' in key.lower()):
					#print('strain: ',data[key][i])
					ni01.age= data[key][i]
				elif ('measurement' in key.lower()):
					print(data[key][i])
					d = data[key][i]
					ni01.measurement_date= d				 
				elif ('clinical' in key.lower()):
					#print('induced: ',data[key][i])
					ni01.clinical_score= data[key][i]
				elif ('comment' in key.lower()):
					#print('induced: ',data[key][i])
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
					#print('genotype: ',data[key][i])
					experiment.timepoint= int(data[key][i])
				elif ('age' in key.lower()):
					#print('strain: ',data[key][i])
					experiment.age= data[key][i]
				elif ('measurement' in key.lower()):
					print(data[key][i])
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
					#print('genotype: ',data[key][i])
					experiment.timepoint= int(data[key][i])
				elif ('measurement' in key.lower()):
					#print(data[key][i])
					d = data[key][i]
					experiment.measurement_date= d				 
				elif ('comment' in key.lower()):
					#print('induced: ',data[key][i])
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

'''def data_iinflc04(data):
	# For all the rows 
	for i in range(2):
		#newAssay = Iinflc04(assayid=a.id)
		for key in data:
			#If mouse find its id from mouse database
			if ('ID' in key):
				print('mouseID: ',data[key][i])
				#newAssay.mid = Mouse.objects.get(mid=data[key][i]).id
			elif ('age' in key.lower()):
				print('age: ',data[key][i])
				#newAssay.age = data[key][i] 			
			elif ('timepoint' in key.lower()):
				print('timepoint: ',data[key][i])
				#newAssay.timepoint = data[key][i] 
			elif ('timepoint type' in key.lower()):
				print('timepoint_type: ',data[key][i]) 
				#newAssay.timepoint_type = data[key][i]
			elif ('measurement' in key.lower()):
				print('measurement_date: ',data[key][i]) 
				#newAssay.measurement_date = data[key][i]
			elif ('weight' in key.lower()):
				print('weight: ',data[key][i]) 
				#newAssay.weight = data[key][i]
		#newAssay.save()
'''
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
	#print("Data")
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

def returnTemplateName(assayobject):
	switcher ={
		5:'assays/assaytypes/iinflc-04.html',
		7:'assays/assaytypes/ni01.html',
		8:'assays/assaytypes/ni02rot01.html',
		9:'assays/assaytypes/ni02ofd01.html'
	}
	return switcher.get(assayobject.id,"Ivalid")
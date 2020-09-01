from .models import *
import openpyxl
from openpyxl import Workbook
import collections

tableNames = ['BIOCHEM-01','BIOCHEM-02','BIOCHEM-03','BIOCHEM-04','BIOCHEM-05',
				'BIOCHEM-06','BIOCHEM-07','BIOCHEM-08','CBA-01','CBA-02','ENDO-01','FC-04',
				'FC-07','HEM-01','HPIBD-01','HPIBD-02','HPIBD-03','HPNI-01','IINFLC-01',
				'IINFLC-02','IINFLC-03','IINFLC-04','NI-01','NI-02_GRS-01','NI-02_OFD-01',
				'NI-02_ROT-01','PR-02',"info"
				]



def create_mouseHash(data):
	for i in range(len(data)):
		m = Mouse()
		print("MOUSE")
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
		m.save()

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
		for r in range(2,rows):
			object = sheet.cell(row=r, column = c).value
			d[r0].append(object)
	return d;

def handle_uploaded_file(fname):
    #with open('some/file/name.txt', 'wb+') as destination:
    #    for chunk in f.chunks():
    #        destination.write(chunk)
	fname = '200601_Phenotypos_EAE_wdwTo90.xlsx'
	fname = '../../../static/media/assays/xlsx/'+fname
	wb = openpyxl.load_workbook(fname)
	info = dataofAssay("info",fname)
	create_mouseHash(info)
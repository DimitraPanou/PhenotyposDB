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
					if(data[key][i] is None):
						flag = 0
						break; 
					mouse = Mouse.objects.get(mid=data[key][i])
					if(mouse): 
						iinflc04.mid = mouse
					else:
						flag = 0
						break;			
				elif ('timepoint' in key.lower()):
					iinflc04.timepoint= data[key][i]
				elif ('age' in key.lower()):
					iinflc04.age= data[key][i]
				elif ('measurement' in key.lower()):
					d = data[key][i]
					iinflc04.measurement_date= d				 
				elif ('weight' in key.lower()):
					iinflc04.weight= data[key][i]
				elif ('comment' in key.lower()):
					iinflc04.comment= data[key][i]
		if(flag):				
			iinflc04.save()

def data_iinflc02(data,assay):
	for i in range(len(data["Mouse ID"])):
		flag =1
		experiment = Iinflc02()
		experiment.assayid = assay
		for key in data:
			if(flag):
				if ('Mouse ID' in key):
					#Return mouse id from mouse table
					#print(data[key][i])
					if(data[key][i] is None):
						flag = 0
						break; 
					mouse = Mouse.objects.get(mid=data[key][i])
					if(mouse): 
						experiment.mid = mouse
					else:
						flag = 0
						break;			
				elif ('timepoint' in key.lower()):
					print(data[key][i])
					experiment.timepoint= data[key][i]
				elif ('Age' in key):
					experiment.age= data[key][i]
				elif ('measurement' in key.lower()):
					d = data[key][i]
					experiment.measurement_date= d				 
				elif ('sample source' in key.lower()):
					experiment.sample_source= data[key][i]
				elif ('total cell' in key.lower()):
					if ('small' in key.lower()):
						experiment.cell_count_s_intestine = data[key][i]
					else:
						experiment.cell_count_l_intestine = data[key][i]
				elif ('comment' in key.lower()):
					experiment.comment= data[key][i]
		if(flag):				
			experiment.save()

def data_iinflc03(data,assay):
	for i in range(len(data["Mouse ID"])):
		flag =1
		experiment = Iinflc03()
		experiment.assayid = assay
		for key in data:
			if(flag):
				if ('Mouse ID' in key):
					#Return mouse id from mouse table
					#print(data[key][i])
					if(data[key][i] is None):
						flag = 0
						break; 
					mouse = Mouse.objects.get(mid=data[key][i])
					if(mouse): 
						experiment.mid = mouse
					else:
						flag = 0
						break;			
				elif ('timepoint' in key.lower()):
					print(data[key][i])
					experiment.timepoint= data[key][i]
				elif ('Age' in key):
					experiment.age= data[key][i]
				elif ('measurement' in key.lower()):
					d = data[key][i]
					experiment.measurement_date= d				 
				elif ('sum intensity' in key.lower()):
					experiment.sum_intensity= data[key][i]
				elif ('net intensity' in key.lower()):
					experiment.net_intensity = data[key][i]
				elif ('mean intensity' in key.lower()):
					experiment.mean_intensity = data[key][i]
				elif ('acquisition' in key.lower()):
					experiment.acquisition_settings = data[key][i]
				elif ('comment' in key.lower()):
					experiment.comment= data[key][i]
		if(flag):				
			experiment.save()

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
					if(data[key][i] is None):
						flag = 0
						break; 
					mouse = Mouse.objects.get(mid=data[key][i])
					if(mouse): 
						ni01.mid = mouse
					else:
						flag = 0
						break;			
				elif ('timepoint' in key.lower()):
					ni01.timepoint= data[key][i]
				elif ('age' in key.lower()):
					ni01.age= data[key][i]
				elif ('measurement' in key.lower()):
					d = data[key][i]
					ni01.measurement_date= d				 
				elif ('clinical' in key.lower()):
					ni01.clinical_score= data[key][i]
				elif ('comment' in key.lower()):
					ni01.comment= data[key][i]
		if(flag):					
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
					if(data[key][i] is None):
						flag = 0
						break; 
					mouse = Mouse.objects.get(mid=data[key][i])
					if(mouse): 
						experiment.mid = mouse
					else:
						flag = 0
						break;			
				elif ('timepoint' in key.lower()):
					experiment.timepoint= data[key][i]
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
		if(flag):				
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
					if(data[key][i] is None):
						flag = 0
						break; 
					mouse = Mouse.objects.get(mid=data[key][i])
					if(mouse): 
						experiment.mid = mouse
					else:
						flag = 0
						break;			
				elif ('timepoint' in key.lower()):
					experiment.timepoint= data[key][i]
				elif ('measurement' in key.lower()):
					d = data[key][i]
					experiment.measurement_date= d				 
				elif ('comment' in key.lower()):
					experiment.comment= data[key][i]
				elif ('Age' in key):
					experiment.age= data[key][i]
				elif ('distance' in key.lower()):
					if('arena' in key.lower()):
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
		if(flag):				
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
					if(data[key][i] is None):
						flag = 0
						break; 
					mouse = Mouse.objects.get(mid=data[key][i])
					if(mouse): 
						experiment.mid = mouse
					else:
						flag = 0
						break;			
				elif ('timepoint' in key.lower()):
					experiment.timepoint= data[key][i]
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
		if(flag):				
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
					if(data[key][i] is None):
						flag = 0
						break; 
					mouse = Mouse.objects.get(mid=data[key][i])
					if(mouse): 
						experiment.mid = mouse
					else:
						flag = 0
						break;			
				elif ('timepoint' in key.lower()):
					experiment.timepoint= data[key][i]
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
		if(flag):
			experiment.save()

def data_biochem01(data,assay):
	for i in range(len(data["Mouse ID"])):
		flag =1
		experiment = Biochem01()
		experiment.assayid = assay
		for key in data:
			if(flag):
				if ('Mouse ID' in key):
					#Return mouse id from mouse table
					#print(data[key][i])
					if(data[key][i] is None):
						flag = 0
						break; 
					mouse = Mouse.objects.get(mid=data[key][i])
					if(mouse): 
						experiment.mid = mouse
					else:
						flag = 0
						break;			
				elif ('timepoint' in key.lower()):
					#print(data[key][i])
					experiment.timepoint= data[key][i]
				elif ('Age' in key):
					experiment.age= data[key][i]
				elif ('measurement' in key.lower()):
					d = data[key][i]
					experiment.measurement_date= d				 
				elif ('sample source' in key.lower()):
					experiment.sample_source= data[key][i]
				elif ('total protein' in key.lower()):
					experiment.total_protein = data[key][i]
				elif ('albumin' in key.lower()):
					experiment.albumin = data[key][i]
				elif ('comment' in key.lower()):
					experiment.comment= data[key][i]
		if(flag):				
			experiment.save()

def data_biochem02(data,assay):
	for i in range(len(data["Mouse ID"])):
		flag =1
		experiment = Biochem02()
		experiment.assayid = assay
		for key in data:
			if(flag):
				if ('Mouse ID' in key):
					#Return mouse id from mouse table
					#print(data[key][i])
					if(data[key][i] is None):
						flag = 0
						break; 
					mouse = Mouse.objects.get(mid=data[key][i])
					if(mouse): 
						experiment.mid = mouse
					else:
						flag = 0
						break;			
				elif ('timepoint' in key.lower()):
					#print(data[key][i])
					experiment.timepoint= data[key][i]
				elif ('Age' in key):
					experiment.age= data[key][i]
				elif ('measurement' in key.lower()):
					d = data[key][i]
					experiment.measurement_date= d				 
				elif ('sample source' in key.lower()):
					experiment.sample_source= data[key][i]
				elif ('sodium' in key.lower()):
					experiment.sodium = data[key][i]
				elif ('potassium' in key.lower()):
					experiment.potassium = data[key][i]
				elif ('chloride' in key.lower()):
					experiment.chloride = data[key][i]
				elif ('phosphorus' in key.lower()):
					experiment.phosphorus = data[key][i]
				elif ('calcium' in key.lower()):
					experiment.calcium = data[key][i]
				elif ('magnesium' in key.lower()):
					experiment.magnesium = data[key][i]
				elif ('comment' in key.lower()):
					experiment.comment= data[key][i]
		if(flag):				
			experiment.save()

def data_biochem03(data,assay):
	for i in range(len(data["Mouse ID"])):
		flag =1
		experiment = Biochem03()
		experiment.assayid = assay
		for key in data:
			if(flag):
				if ('Mouse ID' in key):
					#Return mouse id from mouse table
					#print(data[key][i])
					if(data[key][i] is None):
						flag = 0
						break; 
					mouse = Mouse.objects.get(mid=data[key][i])
					if(mouse): 
						experiment.mid = mouse
					else:
						flag = 0
						break;			
				elif ('timepoint' in key.lower()):
					#print(data[key][i])
					experiment.timepoint= data[key][i]
				elif ('Age' in key):
					experiment.age= data[key][i]
				elif ('measurement' in key.lower()):
					d = data[key][i]
					experiment.measurement_date= d				 
				elif ('sample source' in key.lower()):
					experiment.sample_source= data[key][i]
				elif ('ALT' in key):
					experiment.alt = data[key][i]
				elif ('ALP' in key):
					experiment.alp = data[key][i]
				elif ('AST' in key):
					experiment.ast = data[key][i]
				elif ('bilirubin total' in key.lower()):
					experiment.total_bilirubin = data[key][i]
				elif ('bilirubin direct' in key.lower()):
					experiment.direct_bilirubin = data[key][i]
				elif ('comment' in key.lower()):
					experiment.comment= data[key][i]
		if(flag):				
			experiment.save()

def data_biochem04(data,assay):
	for i in range(len(data["Mouse ID"])):
		flag =1
		experiment = Biochem04()
		experiment.assayid = assay
		for key in data:
			if(flag):
				if ('Mouse ID' in key):
					#Return mouse id from mouse table
					#print(data[key][i])
					if(data[key][i] is None):
						flag = 0
						break; 
					mouse = Mouse.objects.get(mid=data[key][i])
					if(mouse): 
						experiment.mid = mouse
					else:
						flag = 0
						break;			
				elif ('timepoint' in key.lower()):
					#print(data[key][i])
					experiment.timepoint= data[key][i]
				elif ('Age' in key):
					experiment.age= data[key][i]
				elif ('measurement' in key.lower()):
					d = data[key][i]
					experiment.measurement_date= d				 
				elif ('sample source' in key.lower()):
					experiment.sample_source= data[key][i]
				elif ('urea' in key.lower()):
					experiment.urea = data[key][i]
				elif ('uric acid' in key.lower()):
					experiment.uric_acid = data[key][i]
				elif ('creatinine' in key.lower()):
					experiment.creatinine = data[key][i]
				elif ('comment' in key.lower()):
					experiment.comment= data[key][i]
		if(flag):				
			experiment.save()

def data_biochem05(data,assay):
	for i in range(len(data["Mouse ID"])):
		flag =1
		experiment = Biochem05()
		experiment.assayid = assay
		for key in data:
			if(flag):
				if ('Mouse ID' in key):
					#Return mouse id from mouse table
					#print(data[key][i])
					if(data[key][i] is None):
						flag = 0
						break; 
					mouse = Mouse.objects.get(mid=data[key][i])
					if(mouse): 
						experiment.mid = mouse
					else:
						flag = 0
						break;			
				elif ('timepoint' in key.lower()):
					#print(data[key][i])
					experiment.timepoint= data[key][i]
				elif ('Age' in key):
					experiment.age= data[key][i]
				elif ('measurement' in key.lower()):
					d = data[key][i]
					experiment.measurement_date= d				 
				elif ('sample source' in key.lower()):
					experiment.sample_source= data[key][i]
				elif ('amylase' in key.lower()):
					experiment.amylase = data[key][i]
				elif ('lipase' in key.lower()):
					experiment.lipase = data[key][i]
				elif ('glucose' in key.lower()):
					experiment.glucose = data[key][i]
				elif ('comment' in key.lower()):
					experiment.comment= data[key][i]
		if(flag):				
			experiment.save()

def data_biochem06(data,assay):
	for i in range(len(data["Mouse ID"])):
		flag =1
		experiment = Biochem06()
		experiment.assayid = assay
		for key in data:
			if(flag):
				if ('Mouse ID' in key):
					#Return mouse id from mouse table
					#print(data[key][i])
					if(data[key][i] is None):
						flag = 0
						break; 
					mouse = Mouse.objects.get(mid=data[key][i])
					if(mouse): 
						experiment.mid = mouse
					else:
						flag = 0
						break;			
				elif ('timepoint' in key.lower()):
					#print(data[key][i])
					experiment.timepoint= data[key][i]
				elif ('Age' in key):
					experiment.age= data[key][i]
				elif ('measurement' in key.lower()):
					d = data[key][i]
					experiment.measurement_date= d				 
				elif ('sample source' in key.lower()):
					experiment.sample_source= data[key][i]
				elif ('cholesterol' in key.lower()):
					if('hdl' in key.lower()):
						experiment.hdl_cholesterol = data[key][i]
					elif('ldl' in key.lower()):
						experiment.ldl_cholesterol = data[key][i]
					else:
						experiment.cholesterol = data[key][i]
				elif ('triglycerides' in key.lower()):
					experiment.triglycerides = data[key][i]
				elif ('nefa' in key.lower()):
					experiment.nefa = data[key][i]
				elif ('comment' in key.lower()):
					experiment.comment= data[key][i]
		if(flag):				
			experiment.save()

def data_biochem07(data,assay):
	for i in range(len(data["Mouse ID"])):
		flag =1
		experiment = Biochem07()
		experiment.assayid = assay
		for key in data:
			if(flag):
				if ('Mouse ID' in key):
					#Return mouse id from mouse table
					#print(data[key][i])
					if(data[key][i] is None):
						flag = 0
						break; 
					mouse = Mouse.objects.get(mid=data[key][i])
					if(mouse): 
						experiment.mid = mouse
					else:
						flag = 0
						break;			
				elif ('timepoint' in key.lower()):
					#print(data[key][i])
					experiment.timepoint= data[key][i]
				elif ('Age' in key):
					experiment.age= data[key][i]
				elif ('measurement' in key.lower()):
					d = data[key][i]
					experiment.measurement_date= d				 
				elif ('sample source' in key.lower()):
					experiment.sample_source= data[key][i]
				elif ('iron' in key.lower()):
					experiment.iron = data[key][i]
				elif ('uibc' in key.lower()):
					experiment.uibc = data[key][i]
				elif ('ferritin' in key.lower()):
					experiment.ferritin = data[key][i]
				elif ('transferrin' in key.lower()):
					experiment.transferrin = data[key][i]
				elif ('comment' in key.lower()):
					experiment.comment= data[key][i]
		if(flag):				
			experiment.save()

def data_biochem08(data,assay):
	for i in range(len(data["Mouse ID"])):
		flag =1
		experiment = Biochem08()
		experiment.assayid = assay
		for key in data:
			if(flag):
				if ('Mouse ID' in key):
					#Return mouse id from mouse table
					#print(data[key][i])
					if(data[key][i] is None):
						flag = 0
						break; 
					mouse = Mouse.objects.get(mid=data[key][i])
					if(mouse): 
						experiment.mid = mouse
					else:
						flag = 0
						break;			
				elif ('timepoint' in key.lower()):
					#print(data[key][i])
					experiment.timepoint= data[key][i]
				elif ('Age' in key):
					experiment.age= data[key][i]
				elif ('measurement' in key.lower()):
					d = data[key][i]
					experiment.measurement_date= d				 
				elif ('sample source' in key.lower()):
					experiment.sample_source= data[key][i]
				elif ('ldl' in key.lower()):
					experiment.ldl = data[key][i]
				elif ('creatinine' in key.lower()):
					experiment.creatinine_kinase = data[key][i]
				elif ('comment' in key.lower()):
					experiment.comment= data[key][i]
		if(flag):				
			experiment.save()

def data_hpibd02(data,assay):
	for i in range(len(data["Mouse ID"])):
		flag =1
		experiment = Hpibd02()
		experiment.assayid = assay
		for key in data:
			if(flag):
				if ('Mouse ID' == key):
					#Return mouse id from mouse table
					#print(data[key][i])
					if(data[key][i] is None):
						flag = 0
						break; 
					mouse = Mouse.objects.get(mid=data[key][i])
					if(mouse): 
						experiment.mid = mouse
					else:
						flag = 0
						break;			
				elif ('timepoint' in key.lower()):
					experiment.timepoint= data[key][i]
				elif ('measurement date' in key.lower()):
					d = data[key][i]
					experiment.measurement_date= d
				elif ('Age' in key):
					experiment.age= data[key][i]
				elif ('comment' in key.lower()):
					experiment.comment= data[key][i]
				elif ('inflammation score' in key.lower()):
					if('small' in key.lower()):
						experiment.inflammation_small= data[key][i]
					else:
						experiment.inflammation_large= data[key][i]
				elif ('epithelial damage' in key.lower()):
					if('small' in key.lower()):
						experiment.epithelial_small= data[key][i]
					else:
						experiment.epithelial_large= data[key][i]
				elif ('villus/crypt' in key.lower()):
					experiment.vc_ratio= data[key][i]
				elif ('colon length' in key.lower()):
					experiment.colon_length= data[key][i]
				elif ('epithelium flattening' in key.lower()):
					experiment.epithelium_s_flattening= data[key][i]
				elif ('apoptotic bodies' in key.lower()):
					if('small' in key.lower()):
						experiment.apoptotic_s_field= data[key][i]
					else:
						experiment.apoptotic_l_field= data[key][i]
				elif ('goblet cell' in key.lower()):
					if('small' in key.lower()):
						experiment.goblet_s_depletion= data[key][i]
					else:
						experiment.goblet_l_depletion= data[key][i]
				elif ('lumen exf' in key.lower()):
					if('small' in key.lower()):
						experiment.lumen_s_exfoliation= data[key][i]
					else:
						experiment.lumen_l_exfoliation= data[key][i]
				elif ('villus short' in key.lower()):
					experiment.villus_s_short= data[key][i]
				elif ('intestinal gland' in key.lower()):
					experiment.igd_small= data[key][i]
				elif ('paneth activation' in key.lower()):
					experiment.paneth_s_activation= data[key][i]
				elif ('peyer patch' in key.lower()):
					experiment.peyer_s_patch= data[key][i]
				elif ('crypt damage' in key.lower()):
					experiment.crypt_l_damage= data[key][i]
				elif ('endothelial' in key.lower()):
					experiment.endothelial_l_activation= data[key][i]
		if(flag):
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

	switcher ={
		6: data_iinflc02(data,assayobject),
		4: data_iinflc03(data,assayobject),
		5: data_iinflc04(data,assayobject),
		7: data_ni01(data,assayobject),		
		8: data_ni02rot01(data,assayobject),		
		9: data_ni02ofd01(data,assayobject),		
		10: data_ni02grs01(data,assayobject),		
		11: data_hem01(data,assayobject),		
		12: data_hpibd02(data,assayobject),		
		13: data_biochem01(data,assayobject),		
		14: data_biochem02(data,assayobject),		
		15: data_biochem03(data,assayobject),		
		16: data_biochem04(data,assayobject),		
		17: data_biochem05(data,assayobject),		
		18: data_biochem06(data,assayobject),		
		19: data_biochem07(data,assayobject),		
		20: data_biochem08(data,assayobject)		

	}
	switcher.get(assayobject.type.id,"Ivalid")


'''
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
	if(assayobject.type.code == "IINFLC-02"):
		data_iinflc02(data,assayobject)
	if(assayobject.type.code == "IINFLC-03"):
		data_iinflc03(data,assayobject)
	if(assayobject.type.code == "HPIBD-02"):
		data_hpibd02(data,assayobject)
	if(assayobject.type.code == "BIOCHEM-01"):
		data_biochem01(data,assayobject)
	if(assayobject.type.code == "BIOCHEM-02"):
		data_biochem02(data,assayobject)
	if(assayobject.type.code == "BIOCHEM-03"):
		data_biochem03(data,assayobject)
	if(assayobject.type.code == "BIOCHEM-04"):
		data_biochem04(data,assayobject)
	if(assayobject.type.code == "BIOCHEM-05"):
		data_biochem05(data,assayobject)
	if(assayobject.type.code == "BIOCHEM-06"):
		data_biochem06(data,assayobject)
	if(assayobject.type.code == "BIOCHEM-07"):
		data_biochem07(data,assayobject)
	if(assayobject.type.code == "BIOCHEM-08"):
		data_biochem08(data,assayobject)
'''
def returnTemplateName(assayobject):
	switcher ={
		5:'assays/assaytypes/iinflc-04.html',
		7:'assays/assaytypes/ni01.html',
		8:'assays/assaytypes/ni02rot01.html',
		9:'assays/assaytypes/ni02ofd01.html'
	}
	return switcher.get(assayobject.id,"Ivalid")
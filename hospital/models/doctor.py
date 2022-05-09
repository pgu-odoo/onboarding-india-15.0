# -*- coding: utf-8 -*-
from odoo import models,fields,api,_



class HospitalDoctor(models.Model):

	_name = 'hospital.doctor'
	_description = 'Hospital Doctor'
	_inherits = {'hospital.patient': 'related_patient'} #all 'hospital.patient' fields will be visiable in this  


	doctor_name  = fields.Char(string="Doctor Name")

	related_patients=fields.Char(string="related_patient")  #this field visiable when the debug mode is activated

	gender=fields.Selection([('male','Male'),('female','Female'),('other','Other')], required=True )
	description=fields.Text(string='Description')
	age=fields.Char(string='Age')

	# patient_ids=fields.Many2many(string='Patients','hospital.patient')   
	#instead of create a field into this table(hospital.doctor) it(many2many) will create a new table which name is "hospital_doctor_hospital_patient_rel" having 2 fields(Foreign Key) of those model

	# patient_ids=fields.Many2many('hospital.patient', 'doctor_patient_rel(table_name)','doctor_id(col_name)','patient_id(col_name)', string='Patients')
	#in somecase(genere a table name is too long psql can contain only 63 char table name so if we craete two or more many2many fiels with same relation) where we have to specify table name like this



	

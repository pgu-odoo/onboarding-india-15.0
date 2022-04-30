# -*- coding: utf-8 -*
{
	'name':' Odoo Hospital',
	'summary':'Hospital',
	'description':""" Hospital:
						- Patientsbar
						- Doctors
					
				""" ,
	'author':'odoo',
	'website':'https://www.odoo.com',
	'category':'Training',
	'version':'0.1',
	'depends':['base_setup','mail'],
	'installable':True,
	'data':[
		'security/ir.model.access.csv',
		'security/hospital_security.xml',
		
		'views/patients_view.xml',	
		'views/hospital_menuitem.xml',
		'views/kids_view.xml',
		'views/patients_gender_view.xml',
		'views/appointment_view.xml',
		
	],
	'demo':[
		'demo/hospital_demo.xml',
		'demo/patients_sequence.xml',
	]
}
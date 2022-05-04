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
	'author':'Vishal Sakariya(visa)',	
	'version':'0.1',
	'depends':['base_setup','mail','web_cohort','base','board'],
	'installable':True,
	'data':[ #security>data>wizard>views
		'security/ir.model.access.csv',
		'security/hospital_security.xml',
		'wizard/create_appointment.xml',
		'views/patients_view.xml',	
		'views/hospital_menuitem.xml',
		'views/kids_view.xml',
		'views/patients_gender_view.xml',
		'views/appointment_view.xml',
		'views/dashboard_view.xml',
		'demo/patients_sequence.xml',
		
	],
	'demo':[
		'demo/hospital_demo.xml',
	]
}
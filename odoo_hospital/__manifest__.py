# -*- coding: utf-8 -*
{
	'name':' Odoo Hospital',
	'summary':'Hospital',
	'description':""" Hospital:
						- Patients
						- Doctors
					
				""" ,
	'author':'odoo',
	'website':'https://www.odoo.com',
	'category':'Training',
	'version':'0.1',
	'depends':['base_setup'],
	'installable':True,
	'data':[
		'security/hospital_security.xml',
		'security/ir.model.access.csv',	
		'views/hospital_menuitem.xml',
		'views/patients_view.xml',
	],
	'demo':[
		'demo/hospital_demo.xml',
	]
}
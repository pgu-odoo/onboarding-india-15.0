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
	'depends':['base_setup','mail','web_cohort','base','board','sale','website_payment'],
	'installable':True,
	'data':[ #security>data>wizard>views>report
		'security/ir.model.access.csv',
		'security/hospital_security.xml',
		'wizard/create_appointment.xml',
		'views/patients_view.xml',	
		'views/hospital_menuitem.xml',
		'views/kids_view.xml',
		'views/patients_gender_view.xml',
		'views/appointment_view.xml',
		'views/dashboard_view.xml',
		'views/doctor_view.xml',
		'views/sale.xml',
		'views/template.xml',
		'demo/patients_sequence.xml',
		'report/report.xml',
		'report/patient_card.xml',
		'report/patient_detail_template.xml',
		
	],
	'demo':[
		'demo/hospital_demo.xml',
	]
}
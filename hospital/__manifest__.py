# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
	'name' : 'hospital',

	'summary' : """hospital based module etc..""",

	'description' : """
		Application for hospital based work:
		-Public Sector
		-Private Housing
	""",

	'author' : 'Odoo',

	'website' : 'https://www.odoo.com',

	'category' : 'Sales',
	'version' : '1.0',

	'depends' : ['base'],  
    

	
	'installable': True,
	'application':True,
	'auto_install': False,
	'license':'LGPL-3',
	'data' : [
			  'security/hospital_security.xml',	
			  'security/ir.model.access.csv',
			  'views/patient.xml',
			  'views/views_of_hospital_patient.xml',

			  ],


	'demo' : ['demo/patient_demodata.xml',],
}
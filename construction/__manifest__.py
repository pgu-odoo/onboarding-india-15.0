# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
	'name' : 'construction',

	'summary' : """construction based module etc..""",

	'description' : """
		Application for construction based work:
		-Public Sector
		-Private Housing
		-Skyhigh Projects
	""",

	'author' : 'Odoo',

	'website' : 'https://www.odoo.com',

	'category' : 'Sales',
	'version' : '1.0',

	'depends' : ['sale','sale_management'],  #we want to inherit from "sale" 
    

	
	'installable': True,
	'application':True,
	'auto_install': False,
	'license':'LGPL-3',
	'data' : [
				'security/academy_security.xml',  #keep sequence like this security related file,data related file,wizaed and last views 
				'security/ir.model.access.csv',
				'wizard/create_appointment.xml',  # watch 31.how to create wizard  in odoo (odoo meta )

				'views/course_views.xml',
				'views/academy_menuitems.xml',
				'views/suject_details.xml',
				'views/sale_views_inherit.xml',
				'report/report.xml',
				'report/print.xml'

			],

	'demo' : ['demo/academy_demo.xml',],
}
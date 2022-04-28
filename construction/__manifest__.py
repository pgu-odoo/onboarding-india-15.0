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

	'depends' : ['sale'],  #we want to inherit from "sale" 
    

	################### commented because it was causing problems in further tasks
	
	'installable': True,
	'application':True,
	'auto_install': False,
	'license':'LGPL-3',
	'data' : [
				'security/academy_security.xml',
				'security/ir.model.access.csv',
				'views/course_views.xml',
				'views/academy_menuitems.xml',
				'views/suject_details.xml',
				'views/sale_views_inherit.xml',

			],

	'demo' : ['demo/academy_demo.xml',],
}
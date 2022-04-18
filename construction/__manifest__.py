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

	'depends' : ['base_setup'],
    

	################### commented because it was causing problems in further tasks
	
	'installable': True,
	'application':True,
	'auto_install': False,
	'license':'LGPL-3',
	'data' : [],
	'demo' : [],
}
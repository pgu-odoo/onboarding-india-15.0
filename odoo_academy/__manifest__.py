#_*_ coding: utf-8 _*_

{
	'name' : 'Odoo Academy' , 

	'summary' : """Academy app to manage Training""" ,

	'description' : """
		Academy module to manage Training:
		- Courses
		- sessions
		- Attendes
	""",

	'author' : 'Odoo' , 

	'website' : 'https://www.odoo.com',

	'category' : 'Training',

	'version' : '0.1' ,

	'depends' : ['base', 'sale','website'],

	'data' : [
		'security/academy_security.xml',
		'security/ir.model.access.csv',
		'views/academy_menuitems.xml',
		'views/course_views.xml',
		'views/session_views.xml',
		'views/sale_views_inherit.xml',
		'views/product_views_inherit.xml',
		'wizard/sale_wizard_view.xml',
		'report/session_report_templates.xml',
		'views/academy_web_templates.xml',
	],

	'demo' : [
		'demo/academy_demo.xml'
	],
	
    'license': 'LGPL-3',
	
}
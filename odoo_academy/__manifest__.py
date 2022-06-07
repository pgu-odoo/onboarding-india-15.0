# -*- coding: utf-8 -*-

{
	'name': 'Odoo Academy',

	'summary': """ Academy app for learning """,

	'description': """ 
		Academy module for learning 
	""",

	'author': 'Odoo',

	'website': 'https:/www.odoo.com',

	'category': 'Learning',

	'version': '15.0.1',

	'depends': ['sale', 'website'],

	'data':[
		'security/academy_security.xml',
		'security/ir.model.access.csv',
		'views/academy_menuitems.xml',
		'views/course_views.xml',		
		'views/session_views.xml',
		'views/sale_views_inherit.xml',
		'views/product_views_inherit.xml',
		'views/academy_web_templates.xml',
		'wizard/sale_wizard_view.xml',
		'report/session_report_templates.xml',
		'views/addenda_test.xml',

	],

	'demo': [
		'demo/academy_demo.xml',
	],
	'license': 'LGPL-3'
}
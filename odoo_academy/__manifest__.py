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

	'depends': ['base'],

	'data':[
		'security/academy_security.xml',
		'security/ir.model.access.csv',
		'views/academy_menuitems.xml',
		'views/course_views.xml',		
		'views/session_views.xml',		
	],

	'demo': [
		'demo/academy_demo.xml',
	],
	'license': 'LGPL-3'
}
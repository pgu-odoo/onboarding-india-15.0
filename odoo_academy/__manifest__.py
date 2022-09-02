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

	'depends' : ['base'],

	'data' : [
		'security/academy_security.xml',
		'security/ir.model.access.csv',
		'views/academy_menuitems.xml',
	],

	'demo' : [
		'demo/academy_demo.xml'
	],
	
    'license': 'LGPL-3',
	
}
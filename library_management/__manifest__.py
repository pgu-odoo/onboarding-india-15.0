#_*_ coding: utf-8 _*_

{
	'name' : 'Library Management' , 

	'summary' : """Management app to manage library""" ,

	'description' : """
		Management Module to manage library:
		- Book
		- sessions
		- Attendes
	""",

	'author' : 'Odoo' , 

	'website' : 'https://www.odoo.com',

	'category' : 'Training',

	'version' : '0.1' ,

	'depends' : ['base'],

	'data' : [
		'security/library_security.xml',
		'security/ir.model.access.csv',
		'views/library_menuitems.xml',
		'views/book_views.xml',
		'views/rentals_views.xml',
	],

	'demo' : [
		'demo/library_demo.xml'
	],
	'license': 'LGPL-3',
}
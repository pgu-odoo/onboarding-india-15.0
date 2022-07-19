# -*- coding: utf-8 -*-
{
	'name': 'Medi Zone',
	'version': '1.0',
	'sequence': 1,
	'category': 'Medi Zone',
	'website': 'http://www.odoo.com/',
	'summary': """E-commerce for medicine orders""",
	'depends':['base', 'base_setup','product','web'],
	
	'assets':{
		'web.assets_backend_prod_only':[
			'medi_zone/static/src/main.js',
		],
		'web.assets_backend':[
			'medi_zone/static/src/widgets/shop.js',
			
		],
	},
	'data': [
			
		 	'views/mart_menuitem.xml',
		 	'security/ir.model.access.csv'
	],
 
	'demo': [],
	'installable': True,
	'application': True,

	'license': 'LGPL-3',
}
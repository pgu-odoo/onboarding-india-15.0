# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
	'name' : 'Estate',

	'summary' : """Real Estates based module""",

	'description' : """
		Application for Real Estate based work:
		-Public Sector
		-Private Housing
		-Skyhigh Projects
	""",

	'author' : 'Odoo',

	'website' : 'www.odoo.com',

	'category' : 'Sales',
	'version' : '1.0',
	'license' : 'LGPL-3',

	'depends' : ['base'],

	'data' : [
		'security/estate_security.xml',
		'security/ir.model.access.csv',
		'views/real_estate_property_view.xml',
		'views/real_estate_property_menu.xml',
		'views/real_estate_property_type.xml',
		'views/real_estate_property_tag.xml',
		'views/real_estate_property_offer.xml',
	],

	'demo' : [
		'demo/estate_demo.xml',

	],
	'auto_install' : True,
	'application': True,
}
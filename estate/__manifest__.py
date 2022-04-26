# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details. a dictionary, each key in this dctionary is module
{
    'name' : 'Real Estate',
    'version' : '1.0',
    'summary': 'A consolidated tool for Estate management',
    'sequence': 1002,
    'description': """  A complete module for Estate managemnet
    and organizing """,
    'category': 'Real Estate',
    'depends' : ['base'],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
    'data':['security/ir.model.access.csv',
    'views/estate_property_views.xml',
    'views/estate_menu.xml',],
}
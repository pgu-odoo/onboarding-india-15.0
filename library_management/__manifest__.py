# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'Library Management',
    'summary': 'local library to manage books and customers',
    'description': "modue for library management",
    'depends': ['base'],
    'author': 'mihir soni',
    'category': 'management',
    'version':'15.0.1.0.0',
    'data': [
        'security/security_management.xml',
        'security/ir.model.access.csv',
        'views/academy_menuitems.xml',
    ],
    'license': 'LGPL-3',
    'demo': [
        'demo/library_management.xml',
    ],
}

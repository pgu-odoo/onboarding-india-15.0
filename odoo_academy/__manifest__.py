# -*- coding: utf-8 -*-

{
    'name': 'Odoo Academy',
    'version': '1.0',
    'description': """test odoo""",
    'depends': ['base'],
    'data': [
        'security/academy_security.xml',
        'security/ir.model.access.csv',
        'views/academy_menuitems.xml',
        'views/course_views.xml',
        'views/session_views.xml',
    ],

    'demo':[
        'demo/academy_demo.xml',
    ],
    
    'installable': True,
    'license': 'LGPL-3',
}

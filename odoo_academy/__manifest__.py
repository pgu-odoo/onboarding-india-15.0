# -*- coding: utf-8 -*-

{
    'name': 'Odoo Academy',
    'version': '1.0',
    'description': """test odoo""",
    'depends': ['sale','website'],
    'data': [
        'security/academy_security.xml',
        'security/ir.model.access.csv',
        'views/academy_menuitems.xml',
        'views/course_views.xml',
        'views/session_views.xml',
        'views/sale_views_inherit.xml',
        'views/product_views_inherit.xml',
        'wizards/sale_wizard_view.xml',
        'report/session_report_templates.xml',
        'views/academy_web_templates.xml',
        'views/addenda_test.xml',
    ],

    'demo':[
        'demo/academy_demo.xml',
    ],
    

    'installable': True,
    'license': 'LGPL-3',
}

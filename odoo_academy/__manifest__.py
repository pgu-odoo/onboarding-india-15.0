# -*- coding: utf-8 -*-
{
    'name':' Odoo Acedamy',
    'summary':""" Acedamy app to manage training""",
    'description':""" Acedamy app to manage training:
                        - courses
                        - sessions
                        - attendees
                """ ,
    'author':'odoo',
    'website':'https://www.odoo.com/',
    'category':'Training',
    'version':'0.1',
    'depends':['sale','base'],
    'installable':'True',
    'data':[
        'security/academy_security.xml',
        'security/ir.model.access.csv',
        'views/academy_menuitems.xml',
        'views/course_views.xml',
        'views/session_views.xml',
        'views/sale_views_inherit.xml',
        'views/product_views_inherit.xml',
        'wizard/sale_wizard_view.xml',
        ],
    'demo':['demo/academy_demo.xml',
    ]

}

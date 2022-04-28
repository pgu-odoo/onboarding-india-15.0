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
    'depends':['base_setup'],
    'installable':'True',
    'data':[
        'security/academy_security.xml',
        'security/ir.model.access.csv',
        'views/academy_menuitems.xml',
        'views/course_views.xml',],
    'demo':['demo/academy_demo.xml',
    ]

}

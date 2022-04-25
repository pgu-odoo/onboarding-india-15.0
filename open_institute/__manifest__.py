# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details. a dictionary, each key in this dctionary is module
{
    'name' : 'Odoo Open Institue',
    
    'summary': """Open institute Mission""",

    'sequence': 1100,
    
    'description': """  Academy module to manage training:
    -courses
    -sessions
    -attendences.""",
 
    'author': 'Odoo',

     'website': 'https://Odoo.com',

    'category': 'Training',
  
    'depends' : ['sale'],
  

    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',


    'data':[
      'security/institute_security.xml',
      'security/ir.model.access.csv',
      'views/institute_menu_item.xml',
      'views/course_views.xml',
      'views/session_view.xml',
      'views/sales_view_inherit.xml',
      'views/product_view_inherit.xml',
      'wizard/sale_wizard_view.xml',
      'report/session_report_template.xml',
    ],

    'demo': ['demo/institute_demo.xml',],
}
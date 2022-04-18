# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details. a dictionary, each key in this dctionary is module
{
    'name' : 'Odoo Open Institue',
    
    'summary': """Open institute Mission""",

    'sequence': 1100,
    
    'description': """  Academy module to manage training:
    -courses
    -sessions
    -attendences.
                  """,
 
     'author': 'Odoo',

     'website': 'https://Odoo.com',

    'category': 'Training',
  
    'depends' : ['base_setup'],
  

    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',


    'data':[
      'security/institute_security.xml',
      'security/ir.model.access.csv',
    ],


    'demo' : [ 'demo/institute_demo.xml',

    ],
}
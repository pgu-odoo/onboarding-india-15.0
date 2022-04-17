# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details. a dictionary, each key in this dctionary is module
{
    'name' : 'Odoo Open Institue',
    'version' : '1.0',
    'summary': 'Open institute Mission',
    'sequence': 999,
    'description': """  Academy module to manage training:
    -courses
    -sessions
    -attendences.
                  """,
    'category': 'Planning/Sales/Contacts',
    'depends' : ['base_setup'],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
    'data':[,
    ],

    'demo' : [ 'demo/institute_demo.xml',],
}
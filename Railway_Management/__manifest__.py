# -*- coding: utf -8 -*-

{
    'name' : 'Railway Management',
    'version' : '1.0',
    'description': "Railway management" ,
    'sequence':'-100',
    'website':"www.irctc.co.in",
    'author':"Odoo",
    'summary':"Railway Management Software",
    'category': 'Management',
     'license': 'LGPL-3',
    'depends' : ['base'],
    'data':[
            'security/security.xml',
            'security/ir.model.access.csv',
            'views/passengers_view.xml',
    ],
    'demo' : [

    ],
    'installable' : True,
    'application': True,
    'auto_install': False,
}
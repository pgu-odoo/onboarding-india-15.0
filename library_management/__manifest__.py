{
    'name': "Library Management",
    'version': '1.0',
    'summary' : """Manage the books""",
     'description': """
         Library Management for manage the books
      """,
      'author': "odoo",

     'website': 'https://www.odoo.com',
     'category' : 'Management',

     'depends': ['base'],

     'data': [
        'security/library_security.xml',
        'security/ir.model.access.csv',
        'views/library_menuitem.xml',
        'views/book_views.xml',
       
        
     ],

     'demo': [
        'demo/Library.demo.xml',
     ],
    
}
#-*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

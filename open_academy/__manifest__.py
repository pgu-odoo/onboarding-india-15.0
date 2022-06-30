
# -*- coding: utf-8 -*-

{
    'name' : 'Open Academy',
    'version' : '1.0',
    'summary': 'Module for testing',
    'sequence': 1,
    'description': """testing""",
    'website': 'https://www.odoo.com/',
    'depends' : ['sale'],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',

    'data': [
    'security/academy_security.xml',
    'security/ir.model.access.csv',
    'views/academy_menuitem.xml',
    'views/course_view.xml',
    'views/session_view.xml',
    'views/sale_views_inherit.xml',
    'views/product_views_inherit.xml',
    'wizard/sale_wizard_view.xml',
    'report/session_report_templates.xml',],
    
    'demo':[
    'demo/academy_demo.xml',],
   }

{
    'name' : 'Open Vadilal',
    'version' : '1.0',
    'summary': 'Module for testing',
    'sequence': 1,
    'description': """testing""",
    'website': 'https://www.odoo.com/',
    'depends' : ['base_setup'],
    'data': [
    'security/vadilal_security.xml',
    'security/ir.model.access.csv',
    'views/vadilal_menuitem.xml',
    'views/categories_view.xml',
    'views/session_view.xml',],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',

    'demo':[
    'demo/vadilal_demo.xml',],
    
}
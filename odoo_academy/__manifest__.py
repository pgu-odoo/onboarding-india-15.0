{
    'name': 'odoo_academy',
    'version': '15.0',
    'summary': 'day one technical training',
    'description': 'description for the module',
    'author': 'Test',
    'website': 'odoo.com',
    'depends': ['base'],
    'data': [
        'security/academy_security.xml',
        'security/ir.model.access.csv',
        'views/academy_menuitems.xml'
    ],
    'demo':
    ['demo/academy_demo.xml'],

    'installable': True,
    'auto_install': False
}

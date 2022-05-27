{
    'name': 'odoo_academy',
    'version': '15.0',
    'summary': 'day one technical training',
    'description': 'description for the module',
    'author': 'Test',
    'website': 'odoo.com',
    'depends': ['sale'],
    'data': [
        'security/academy_security.xml',
        'security/ir.model.access.csv',
        'views/course_views.xml',
        'views/session_views.xml',
        'views/sale_view_inherit.xml',

    ],
    'demo':
    ['demo/academy_demo.xml'],

    'installable': True,
    'auto_install': False
}

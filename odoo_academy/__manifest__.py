{
    'name': 'odoo_academy',
    'version': '15.0',
    'summary': 'day one technical training',
    'description': 'description for the module',
    'author': 'Test',
    'sequence':-1000,
    'website': 'odoo.com',
    'depends': ['base','product' , 'website'],
    'data': [
        'security/academy_security.xml',
        'security/ir.model.access.csv',
        'views/course_views.xml',
        'views/session_views.xml',
        'views/product_views_inherit.xml',
        'wizard/sale_wizard_view.xml',
        'views/sale_views_inherit.xml',
        'report/session_report_template.xml',
        'views/academy_web_template.xml'
    ],

    'demo':
    ['demo/academy_demo.xml'],

    'installable': True,
    'auto_install': False,
    'application':True,
}

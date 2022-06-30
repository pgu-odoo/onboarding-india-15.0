
{
    'name' : 'Odoo academy',
    'version' : '1.0',
    'summary': 'App for odoo academy',
    'sequence': 1,
    'description': """Test """,
    'data': [
            'data/acadamy_demo.xml',
            'security/security_acadamy.xml',
            'security/ir.model.access.csv',
            'views/academy_menuitem.xml',
            'views/course_view.xml',
            'views/session_views.xml',
    ],
    'depends': ['base'],            
    'demo': [],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3'
    }
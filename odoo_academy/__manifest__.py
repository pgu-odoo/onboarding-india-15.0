
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
            'views/sale_view_inherit.xml',
            'views/product_view_inherit.xml',
            'wizard/sale_wizard_view.xml',
            'report/session_reports_template.xml',
            'views/acadamy_web_templates.xml'
    ],
    'depends': ['sale','website'],            
    'demo': [],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3'
    }
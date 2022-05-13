{
    'name': 'Hospital Management',
    'version': '15.0.0.1',
    'summary':'Hospital Management Software',
    'sequence': -100,
    'description': """Hospital Mangement Software""",
    'category': 'Management',
    'website': 'https://www.odoo.com',
    'license': 'LGPL-3',
    'depends': ['base','mail','board','sale'],
    'data': [
        'security/hospital_security.xml',
        'security/ir.model.access.csv',
        'data/patient_sequence.xml',
        'views/patient_view.xml',
        'views/doctor_view.xml',
        'views/bill_view.xml',
        'views/configuration_view.xml',
        'views/appointment_view.xml',
        'views/dashboard_view.xml',
        'views/sale_inherited_view.xml',
        'views/product_views_inherit.xml',
        'views/patient_wizard_view.xml',
        ],
'demo': [
    'demo/demo.xml',
],
    'installable': True,
    'application': True,
    'auto_install': False,
}

{
    'name': 'library_management_system',
    'version': '14.0',
    'description': 'Library management system',
    'summary': 'managing the books issued and reserved ',
    'author': 'ashish',
    'website': 'http://odoo.com',
    'depends': ['base'],
    'data': [
        'security/library_security.xml',
        'security/ir.model.access.csv',
        'views/books_views.xml',
    ],

    'installable':  True,
    'auto_install': False
}


{
    'name': 'library_management',
    'version': '1.0',
    'description': 'Library management system',
    'summary': 'store the information about books ',
    'author': 'Shamy',
    'website': 'http://odoo.com',
    'depends': ['base'],

    'data':[
            'data/book_data.xml',
            'security/security_library.xml',
            'security/ir.model.access.csv',
            'view/library_menuitem.xml',
            'view/library_view.xml',
            'view/rent_views.xml',
    ],
    'depends': ['base'], 
    'installable':  True,
    'auto_install': False,
    'license': 'LGPL-3'

}
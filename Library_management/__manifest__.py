
{
    'name': 'library_management',
    'version': '1.0',
    'description': 'Library management system',
    'summary': 'store the information about books ',
    'author': 'Shamy',
    'website': 'http://odoo.com',
    'depends': ['base','web_map','website'],

    'data':[
            'data/book_data.xml',
            'security/security_library.xml',
            'security/ir.model.access.csv',
            'view/library_menuitem.xml',
            'view/library_view.xml',
            'view/rent_views.xml',
            'view/library_book_copy_inherits.xml',
            'wizard/book_wizard.xml',
            'view/book_web_template.xml'
    ],
    'installable':  True,
    'auto_install': False,
    'license': 'LGPL-3'

}
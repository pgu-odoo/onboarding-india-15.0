{
    'name': 'Odoo Shop',
    'version': '0.1',
    'sequence': 1,
    'category': 'Odoo Shop',
    'summary': """Odoo Online Shop""",
    'depends': [
        'base', 'product', 'web'
    ],
    'data': [
        # static data go here
        'views/shop_menu.xml',
    ],
    'assets': {
        # 
    },
    'demo': [],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}
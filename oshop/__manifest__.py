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
        'data/shop_product_data.xml',
        'views/shop_menu.xml',
        'views/product_view.xml',
        'security/ir.model.access.csv',
    ],
    'assets': {
        'web.assets_backend_prod_only': [
            'oshop/static/src/main.js',
        ],
        'web.assets_backend': [
            'oshop/static/src/widgets/o_shop.js',
            'oshop/static/src/widgets/shop.scss',
        ],
    },
    'demo': [],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}
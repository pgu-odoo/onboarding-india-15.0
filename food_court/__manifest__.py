# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name' : 'Food Court',
    'version' : '0.1',
    'sequence': 1,
    'category': 'Food court',
    'website' : 'https://www.odoo.com/',
    'summary' : """E-commerce for lunch orders
""",
    'depends': [
        'base', 'base_setup', 'product', 'web'
    ],
    'data': [
        'data/food_court_data.xml',
        'views/food_court_menu_views.xml',
        'views/product_views.xml',
        'security/ir.model.access.csv',
    ],
    'assets': {
        'web.assets_backend_prod_only': [
            'food_court/static/src/main.js',
        ],
        'web.assets_backend': [
            'food_court/static/src/widgets/shop.js',
            'food_court/static/src/widgets/shop.scss',
        ],
        'web.qunit_suite_tests': [
            'food_court/static/tests/food_court_tests.js',        
        ],
    },
    'demo': [],
    'installable': True,
    'application': True,

    'license': 'LGPL-3',
}

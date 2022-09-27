# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': "Uanalyist_loyalt_program",
    'summary': """Loyalty Points for the Sale""",
    'description': """This module allows you to define a loyalty points in the sale, where customers earn loyalty points and get discount.""",
    'category': 'Custom Development',
    'version': '14.0.1.0',
    'depends': ['base', 'sale_management'],
    'data': [
        'data/cron.xml',
        'security/ir.model.access.csv',
        'wizard/loyalty_redemption_transaction_views.xml',
        'views/loyalt_config_views.xml',
        'views/loyalty_program_transaction_views.xml',
        'views/loalty_program_ranking_views.xml',
        'views/res_config_settings.xml',
        'views/res_partner_views.xml',
        'views/sale_invoice.xml',
        'views/views.xml',
    ],
    'demo': [
        'demo/transaction_sequence.xml',
    ],
}

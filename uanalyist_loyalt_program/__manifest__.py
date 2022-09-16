# -*- coding: utf-8 -*-
{
    'name': "Uanalyist_loyalt_program",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'sale_management', 'sale'],

    # always loaded
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
    # only loaded in demonstration mode
    'demo': [
        'demo/transaction_sequence.xml',
    ],
}

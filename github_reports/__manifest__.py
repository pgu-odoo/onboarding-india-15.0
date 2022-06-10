# -*- coding: utf-8 -*-
{
    'name':'Github Reports',
    'sequence': 1,
    'version': '15.0',
    'summary': 'Fetch github data for PR and its summary',
    'description': 'Fetch github data for PR and its summary',
    'category': 'Reports',
    'website': 'https://www.odoo.com/', 
    'data':[
            'views/github_reports_menu_views.xml',
            'views/github_team_views.xml',
            'views/pull_request_views.xml',
            'views/res_partner_views.xml',
            'security/ir.model.access.csv',
            'data/cron.xml'
    ],
    'depends': [ 'mail', 'contacts' ],
    'application':True,
    'installble':True,
    'license': 'OEEL-1',
}
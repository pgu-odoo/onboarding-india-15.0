# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

import time
from datetime import date
from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class LoyaltyProgramConfig(models.Model):
    _name = 'loyalty.program.config'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string='Name', required=True, tracking=True)
    active = fields.Boolean('Active', default=True, tracking=True)
    from_date = fields.Date('From Date', default=time.strftime('%Y-01-01'))
    to_date = fields.Date('To Date', default=time.strftime('%Y-12-31'))
    role = fields.Selection([
        ('doctor', 'Doctor'),
        ('customer', 'Customer'),
    ], 'Role', required=True,)
    based_on_state = fields.Selection([
        ('a', 'Product'),
        ('c', 'order'),
    ], 'Based on',required=True, )
    company_id = fields.Many2one(comodel_name='res.company', string='Company', store=True, default=lambda self: self.env.company.id)
    company_currency_id = fields.Many2one(string='Company Currency', readonly=True, related='company_id.currency_id')
    min_order_value = fields.Monetary(string='Min Order Value', currency_field='company_currency_id')
    point_earned_on_criteria = fields.Float(string='Points Earned Based On Criteria')

    @api.constrains('to_date','from_date')
    def _constrains_min_max(self):
        for record in self:
            if record.from_date and record.to_date:
                if record.to_date < record.from_date or record.from_date > record.to_date:
                    raise ValidationError(_("To Date Must be Greater than From Date"))

    @api.model
    def _autocheck_enddate(self):
        ''' This method is called from a cron job.
        It is used to deactived loyalty program configure if it is over'''

        records = self.search([])
        for rec in records:
            if rec.to_date < date.today():
                print('\n\n end date is finished')
                rec.active = False
        print('call _autocheck_enddate',records)

# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import models, fields, api, _


class LoyaltyProgramTransaction(models.Model):
    _name = 'loyalty.program.transaction'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string='Name', index=True, required=True, )
    partner_id = fields.Many2one('res.partner', string='Contact')
    date = fields.Date(string='Date')
    points = fields.Integer(string='Points')
    operation_type = fields.Selection([
        ('adding', 'Adding Points'),
        ('redemption', 'Redemption')], 'Type', index=True, )
    adds = fields.Integer(string='Add')
    redemption = fields.Integer(string='Redemption')
    balance = fields.Float(string='Balance')
    sale_invoice_id = fields.Many2one('account.move', string='Sale Invoice')
    description = fields.Text('Description')

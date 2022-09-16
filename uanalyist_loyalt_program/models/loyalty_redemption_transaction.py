# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import models, fields, api, _


class LoyaltyRedemptionTransaction(models.Model):
    _name = 'loyalty.redemption.transaction'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    partner_id = fields.Many2one('res.partner')
    sale_order_id = fields.Many2one('sale.order')
    points = fields.Integer(string='Points')
    balance = fields.Integer(string='Balance')
    redemption_value = fields.Integer(string='Redemption Value')

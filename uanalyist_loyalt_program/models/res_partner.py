# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import models, fields, api, _


class ResPartner(models.Model):
    _inherit = "res.partner"

    partner_points = fields.Float(help='The amount of Loyalty points the customer/doctor won with their order')
    partner_balance_points = fields.Float(help='The amount of Loyalty points the customer/doctor won or lost with their order')
    rank_type = fields.Selection([
        ('silver', 'Silver'),
        ('gold', 'Gold')], 'Ranking Type')

    def open_partner_transactions(self):
        return {
            'name': _('Loyalty Transactions'),
            'type': 'ir.actions.act_window',
            'res_model': 'loyalty.program.transaction',
            'view_type': 'tree',
            # 'view_mode': 'form',
            'view_id': self.env.ref('uanalyist_loyalt_program.loyalty_transaction_tree_view').id,
            'views': [(self.env.ref('uanalyist_loyalt_program.loyalty_transaction_tree_view').id, 'tree')],
            'target': 'current',
            'res_id': self.id,
            'context': dict(self._context),
            'domain': [('partner_id', '=', self.id)]
        }

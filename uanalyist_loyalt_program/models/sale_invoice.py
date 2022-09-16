# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import models, fields, api, _


class AccountMove(models.Model):
    _inherit = "account.move"


    def sale_invoice_point_redemption1(self):
        return {
            'name': 'Redeem Pointsss',
            'res_model': 'loyalty.redemption.transaction.wizard',
            'type': 'ir.actions.act_window',
            'context': {
                'default_partner_id': self.partner_id.id,
                'default_sale_invoice': self.id,
                'default_partner_id_points': self.partner_id.partner_balance_points,
                'default_balance': 1,
            },
            'view_mode': 'form',
            # 'view_type': 'form',
            'view_id': self.env.ref("uanalyist_loyalt_program.loyalty_redemption_transaction_wizard_form_view").id,
            'target': 'new'
        }
    def clear_points(self):
        self.partner_id.partner_points = self.partner_id.partner_balance_points = 0.0

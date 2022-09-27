# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import models,fields,api,_
from odoo.exceptions import UserError


class LoyaltyRedemptionTransactionWizard(models.TransientModel):
    _name = 'loyalty.redemption.transaction.wizard'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    points = fields.Integer(string='Points')

    @api.model
    def default_get(self, fields):
        res = super(LoyaltyRedemptionTransactionWizard, self).default_get(fields)
        res['points'] = self._context['default_partner_id_points']
        return res

    def action_create_redemption(self):
        customer_invoice = self.env['account.move'].browse(self.env.context.get('active_id'))
        if self.points < 1:
            raise UserError('Points input cannot be 0 or negative')
        elif self.points > customer_invoice.partner_id.partner_balance_points:
            raise UserError(_('%s have only %s points for redemption', customer_invoice.partner_id.name,customer_invoice.partner_id.partner_balance_points))
        elif customer_invoice.move_type == "in_invoice":
            price = self.points * self.env.company.value_for_every_point / self.env.company.loyalty_points
            customer_invoice.partner_id.partner_balance_points -= self.points
            invoice_line = {'name': 'redeem loyalty pointys', 'product_id': self.env.company.doctor_product_id,
                            'price_unit': price, 'price_subtotal': price}
        else:
             max_redeemeble_points = customer_invoice.amount_total * self.env.company.loyalty_points / self.env.company.value_for_every_point
             if self.points < max_redeemeble_points:
                 customer_invoice.partner_id.partner_balance_points -= self.points
                 price_deduct = self.points * self.env.company.value_for_every_point / self.env.company.loyalty_points
             if self.points >= max_redeemeble_points:
                 customer_invoice.partner_id.partner_balance_points -= max_redeemeble_points
                 price_deduct = max_redeemeble_points * self.env.company.value_for_every_point / self.env.company.loyalty_points
             invoice_line = {'name': 'redeem loyalty pointys', 'product_id': self.env.company.patients_product_id,
                                 'price_unit': - price_deduct, 'price_subtotal': - price_deduct}
        customer_invoice.write({'invoice_line_ids': [(0, 0, invoice_line)]})

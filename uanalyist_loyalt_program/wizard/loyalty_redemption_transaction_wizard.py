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

    def action_create_redemption1(self):
        customer_invoice = self.env['account.move'].browse(self.env.context.get('active_id'))
        date = fields.Date.today()
        lpc = self.env['loyalty.program.config'].search(
            [('from_date', '<=', date), ('to_date', '>=', date), ('active', '=', True),
             ('min_order_value', '<=', customer_invoice.amount_total)])
        if self.points < 1:
            raise UserError('Points input cannot be 0 or negative')
        elif self.points > customer_invoice.partner_id.partner_balance_points:
            raise UserError(_('%s have only %s points for redemption', customer_invoice.partner_id.name,customer_invoice.partner_id.partner_balance_points))
        else:
             max_redeemeble_points = customer_invoice.amount_total * self.env.company.store_loyalty_points
             if self.points < max_redeemeble_points:
                 customer_invoice.partner_id.partner_balance_points -= self.points
                 price_deduct = self.points / self.env.company.store_loyalty_points
                 points_redeem = self.points
             if self.points >= max_redeemeble_points:
                 customer_invoice.partner_id.partner_balance_points -= max_redeemeble_points
                 price_deduct = max_redeemeble_points / self.env.company.store_loyalty_points
                 print('price_deduct',price_deduct)
                 points_redeem = max_redeemeble_points

             # 'product_id': program.discount_line_product_id.id,
             invoice_line = {'name': 'redeem loyalty pointys', 'product_id': 41,'price_unit': -price_deduct, 'price_subtotal':-price_deduct }
             customer_invoice.write({'invoice_line_ids': [(0, 0, invoice_line)]})
             self.env['loyalty.program.transaction'].create(
                {
                    'name': self.env['ir.sequence'].next_by_code('loyalty.program.transaction.sequence'),
                    'partner_id': customer_invoice.partner_id.id,
                    'date': customer_invoice.invoice_date,
                    'operation_type': 'b',
                    'points': customer_invoice.partner_id.partner_points,
                    'balance': customer_invoice.partner_id.partner_balance_points,
                    'redemption': points_redeem,
                    'sale_invoice_id': customer_invoice.id,
                    'description': 'This Redemption transaction has been created for this partner from his sale order',
                })

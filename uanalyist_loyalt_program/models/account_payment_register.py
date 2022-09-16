# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, models, _


class AccountPaymentRegister(models.TransientModel):
    _inherit = "account.payment.register"


    def action_create_payments(self): #self = account.payment.register(16,)
        res = super(AccountPaymentRegister, self).action_create_payments()
        customer_invoice = self.env['account.move'].browse(self.env.context.get('active_id'))
        date = customer_invoice.invoice_date

        print('\n-------------self.env.context',self.env.context)
        lpcs = self.env['loyalty.program.config'].search(
            [('from_date', '<=', date), ('to_date', '>=', date), ('active', '=', True),
             ('min_order_value', '<=', customer_invoice.amount_total)])

        if lpcs: #loyalty.program.config(1,)
            # rec.loyalty_config_id = lpcs.id
            for lpc in lpcs:
                if lpc.based_on_state == "a" and customer_invoice.invoice_line_ids:  # product
                    for line in customer_invoice.invoice_line_ids:
                        add_points = 0.0
                        add_points += line.quantity * lpc.point_earned_on_criteria
                        customer_invoice.partner_id.partner_points += add_points
                        customer_invoice.partner_id.partner_balance_points += add_points

                if lpc.based_on_state == "c" and customer_invoice.invoice_line_ids:  # order
                    customer_invoice.partner_id.partner_points += lpc.point_earned_on_criteria
                    customer_invoice.partner_id.partner_balance_points += lpc.point_earned_on_criteria
                    # value = customer_invoice.partner_id.partner_balance_points * lpc.value_for_every_point / lpc.point_earned_on_criteria

            lprs = self.env['loyalty.program.ranking'].search([('active', '=', True)])
            for lpr in lprs:
                if lpr.starting_points < customer_invoice.partner_id.partner_points:
                    customer_invoice.partner_id.rank_type = lpr.rank_type

            self.env['loyalty.program.transaction'].create(
                {
                    'name': self.env['ir.sequence'].next_by_code('loyalty.program.transaction.sequence'),
                    'partner_id': customer_invoice.partner_id.id,
                    'date': date,
                    # 'value': value,
                    'points': customer_invoice.partner_id.partner_points,
                    'operation_type': 'a',
                    'adds': add_points,
                    'balance': customer_invoice.partner_id.partner_balance_points,
                    'sale_invoice_id': customer_invoice.id,
                    'description': 'This trasaction has been created due to product amount in order lines',
                })
        return res

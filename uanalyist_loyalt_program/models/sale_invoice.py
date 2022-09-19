# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import models, fields, api, _
import numpy as np
from datetime import date

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

    def action_post(self):
        res = super(AccountMove, self).action_post()
        today = date.today()
        lpcs = self.env['loyalty.program.config'].search(
            [('from_date', '<=', today), ('to_date', '>=', today), ('active', '=', True),
             ('min_order_value', '<=', self.amount_total)])

        if lpcs and self.invoice_line_ids:
            for lpc in lpcs:
                if lpc.based_on_state == "product":  # product
                    for line in self.invoice_line_ids:
                        add_points = 0.0
                        add_points += line.quantity * lpc.point_earned_on_criteria
                        self.partner_id.partner_points += add_points
                        self.partner_id.partner_balance_points += add_points
                if lpc.based_on_state == "order":  # order
                    self.partner_id.partner_points += lpc.point_earned_on_criteria
                    self.partner_id.partner_balance_points += lpc.point_earned_on_criteria

            lprs = self.env['loyalty.program.ranking'].search([('active', '=', True)])
            for lpr in lprs:
                if lpr.starting_points <= self.partner_id.partner_points:
                    self.partner_id.rank_type = lpr.rank_type

            self.env['loyalty.program.transaction'].create(
                {
                    'name': self.env['ir.sequence'].next_by_code('loyalty.program.transaction.sequence'),
                    'partner_id': self.partner_id.id,
                    'date': today,
                    'points': self.partner_id.partner_points,
                    'operation_type': 'adding',
                    'adds': add_points,
                    'balance': self.partner_id.partner_balance_points,
                    'sale_invoice_id': self.id,
                    'description': 'This trasaction has been created due to product amount in invoice lines',
                })











        for line in self.invoice_line_ids:
            if line.price_unit < 0 and line.product_id == self.env.company.store_product:
                points_redeem = np.abs(line.price_unit) * self.env.company.store_loyalty_points / self.env.company.store_value_for_every_point
                self.env['loyalty.program.transaction'].create(
                    {
                        'name': self.env['ir.sequence'].next_by_code('loyalty.program.transaction.sequence'),
                        'partner_id': self.partner_id.id,
                        'date': self.invoice_date,
                        'operation_type': 'redemption',
                        'points': self.partner_id.partner_points,
                        'balance': self.partner_id.partner_balance_points,
                        'redemption': points_redeem,
                        'sale_invoice_id': self.id,
                        'description': 'This Redemption transaction has been created for this partner from his sale order',
                    })
        return res

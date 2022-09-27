# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import models, fields, api, _
from datetime import date


class AccountMove(models.Model):
    _inherit = "account.move"

    doctor_id = fields.Many2one('res.partner', string='Doctor', domain="[('contact_type', '=', 'doctor')]")

    def sale_invoice_point_redemption(self):
        return {
            'name': 'Redeem Pointsss',
            'res_model': 'loyalty.redemption.transaction.wizard',
            'type': 'ir.actions.act_window',
            'context': {
                'default_partner_id_points': self.partner_id.partner_balance_points,
            },
            'view_mode': 'form',
            'view_id': self.env.ref("uanalyist_loyalt_program.loyalty_redemption_transaction_wizard_form").id,
            'target': 'new'
        }

    def action_post(self):
        res = super(AccountMove, self).action_post()
        today = date.today()
        lpcs = self.env['loyalty.program.config'].search(
            [('from_date', '<=', today), ('to_date', '>=', today),
             ('active', '=', True), ('min_order_value', '<=', self.amount_total)])
        if lpcs and self.move_type == "out_invoice":
            add_doctor_points = add_patients_points = 0.0
            for lpc in lpcs:
                if lpc.based_on_state == "product":
                    for line in self.invoice_line_ids.filtered(lambda line: line.price_unit > 0):
                        if lpc.contact_type == 'patients':
                            self.partner_id.partner_points += line.quantity * lpc.point_earned_on_criteria
                            self.partner_id.partner_balance_points += line.quantity * lpc.point_earned_on_criteria
                            add_patients_points += line.quantity * lpc.point_earned_on_criteria
                        if lpc.contact_type == 'doctor' and self.doctor_id:
                            self.doctor_id.partner_points += line.quantity * lpc.point_earned_on_criteria
                            self.doctor_id.partner_balance_points += line.quantity * lpc.point_earned_on_criteria
                            add_doctor_points += line.quantity * lpc.point_earned_on_criteria
                if lpc.based_on_state == "order":
                    if lpc.contact_type == 'patients':
                        self.partner_id.partner_points += lpc.point_earned_on_criteria
                        self.partner_id.partner_balance_points += lpc.point_earned_on_criteria
                        add_patients_points += lpc.point_earned_on_criteria
                    if lpc.contact_type == 'doctor' and self.doctor_id:
                        self.doctor_id.partner_points += lpc.point_earned_on_criteria
                        self.doctor_id.partner_balance_points += lpc.point_earned_on_criteria
                        add_doctor_points += lpc.point_earned_on_criteria

            transaction_values = {'date': today, 'operation_type': 'adding', 'sale_invoice_id': self.id, 'description': 'This trasaction has been created due to product amount in sale invoice',}
            if lpcs.filtered(lambda x: x.contact_type == "patients"):
                transaction_values.update({
                    'name': self.env['ir.sequence'].next_by_code('loyalty.program.transaction.sequence'),
                    'partner_id': self.partner_id.id,
                    'points': self.partner_id.partner_points,
                    'adds': add_patients_points,
                    'balance': self.partner_id.partner_balance_points,
                })
                self.env['loyalty.program.transaction'].create(transaction_values)
            if lpcs.filtered(lambda x: x.contact_type == "doctor"):
                transaction_values.update({
                    'name': self.env['ir.sequence'].next_by_code('loyalty.program.transaction.sequence'),
                    'partner_id': self.doctor_id.id,
                    'points': self.doctor_id.partner_points,
                    'adds': add_doctor_points,
                    'balance': self.doctor_id.partner_balance_points,
                })
                self.env['loyalty.program.transaction'].create(transaction_values)

            lprs = self.env['loyalty.program.ranking'].search([('active', '=', True)])
            for lpr in lprs:
                if lpr.rank_type == 'gold' and lpr.starting_points <= self.partner_id.partner_points:
                    self.partner_id.rank_type = 'gold'
                    break
                elif lpr.rank_type == 'silver' and lpr.starting_points <= self.partner_id.partner_points:
                    self.partner_id.rank_type = 'silver'

        transaction_redeem_values = {'date': today, 'operation_type': 'redemption', 'sale_invoice_id': self.id, 'description': 'This Redemption transaction has been created for partner, from his/her sale invoice',}
        points_redeem = 0.0
        if self.invoice_line_ids.filtered(lambda x: x.product_id == self.env.company.patients_product_id or x.product_id == self.env.company.doctor_product_id):
            for line in self.invoice_line_ids:
                if line.product_id == line.env.company.patients_product_id or line.product_id == line.env.company.doctor_product_id:
                    points_redeem += abs(line.price_unit) * self.env.company.loyalty_points / self.env.company.value_for_every_point
            transaction_redeem_values.update({
                'name': self.env['ir.sequence'].next_by_code('loyalty.program.transaction.sequence'),
                'partner_id': self.partner_id.id,
                'points': self.partner_id.partner_points,
                'redemption': points_redeem,
                'balance': self.partner_id.partner_balance_points,
            })
            self.env['loyalty.program.transaction'].create(transaction_redeem_values)
        return res

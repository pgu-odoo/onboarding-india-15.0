# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models

class AccountMoveLine(models.Model):
    _inherit = "account.move.line"

    def unlink(self):
        partner_id = self.move_id.partner_id
        for rec in self:
            if rec.product_id == rec.env.company.patients_product_id or rec.product_id == rec.env.company.doctor_product_id:
                add_points = abs(rec.price_unit) * rec.env.company.loyalty_points / rec.env.company.value_for_every_point
                partner_id.partner_balance_points += add_points
        return super().unlink()

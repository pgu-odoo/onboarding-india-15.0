# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models
import numpy as np


class AccountMoveLine(models.Model):
    _inherit = "account.move.line"

    def unlink(self):
        partner_id = self.env['res.partner'].browse(self.env.context.get('default_partner_id')) or self.partner_id
        if self.price_unit < 0:
            add_points = self.price_unit * self.env.company.store_loyalty_points / self.env.company.store_value_for_every_point
            partner_id.partner_balance_points = partner_id.partner_balance_points + np.abs(add_points)
        return super().unlink()

# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models
import numpy as np



class AccountMoveLine(models.Model):
    _inherit = "account.move.line"

    def unlink(self):

        print('self.env.context',self.partner_id.display_name)

        if self.price_unit < 0:
            add_points = self.price_unit * self.env.company.store_loyalty_points / self.env.company.store_value_for_every_point
            print('add_points',np.abs(add_points))
            self.partner_id.partner_balance_points = self.partner_id.partner_balance_points + np.abs(add_points)
            print('-->>>>',self.partner_id.partner_balance_points)
        return super().unlink()
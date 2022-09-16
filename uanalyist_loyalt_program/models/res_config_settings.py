# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    loyalty_points = fields.Float(string="Default loyalty", related='company_id.store_loyalty_points', readonly=False)
    value_for_every_point = fields.Monetary(string='Value For Every Point', currency_field='company_currency_id',related='company_id.store_value_for_every_point', readonly=False)

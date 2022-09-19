# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models

class ResCompany(models.Model):
    _inherit = "res.company"

    store_loyalty_points = fields.Float(string="Loyalty Points")
    store_value_for_every_point = fields.Monetary(string="Value For Every Point")
    store_product = fields.Many2one('product.product', string='product')
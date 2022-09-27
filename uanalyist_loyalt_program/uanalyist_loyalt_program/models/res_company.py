# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models
from odoo.exceptions import ValidationError


class ResCompany(models.Model):
    _inherit = "res.company"

    loyalty_points = fields.Float(string="Loyalty Points")
    value_for_every_point = fields.Monetary(string="Value For Every Point")
    patients_product_id = fields.Many2one('product.product', string='product')
    doctor_product_id = fields.Many2one('product.product', string='product')

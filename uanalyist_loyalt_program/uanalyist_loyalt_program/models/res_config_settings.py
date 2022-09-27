# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models
from odoo.exceptions import ValidationError


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    loyalty_points = fields.Float(string="Default loyalty", related='company_id.loyalty_points', readonly=False)
    company_id = fields.Many2one(comodel_name='res.company', string='Company', store=True, default=lambda self: self.env.company.id)
    company_currency_id = fields.Many2one(string='Company Currency', readonly=True, related='company_id.currency_id')
    value_for_every_point = fields.Monetary(related='company_id.value_for_every_point', readonly=False)
    patients_product_id = fields.Many2one('product.product', string='product', related='company_id.patients_product_id', readonly=False, required=True,)
    doctor_product_id = fields.Many2one('product.product', string='product', related='company_id.doctor_product_id', readonly=False, required=True,)

    @api.constrains('value_for_every_point')
    def check_value_for_every_point(self):
        if self.value_for_every_point < 1: raise ValidationError('Values input cannot be 0 or negative')


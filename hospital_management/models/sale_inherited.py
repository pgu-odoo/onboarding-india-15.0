# -*- coding: utf-8 -*-

from odoo import models,fields,api

class SaleOrder(models.Model):
    #_INHERITED SALE
    _inherit = 'sale.order.line'

    #ONE SIMPLE FIELDS
    discount_amount = fields.Float("Discount_Amount",compute="_discount")

    #METHOD FOR COUNT DISCOUNT AMOUNT
    @api.depends('price_unit','discount')
    def _discount(self):
        for order in self:
            order.discount_amount = (order.price_unit  *  order.discount) /100
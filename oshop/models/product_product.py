from odoo import fields, models


class ProductProduct(models.Model):
    _inherit = 'product.product'

    check = fields.Boolean(string="Check OK")
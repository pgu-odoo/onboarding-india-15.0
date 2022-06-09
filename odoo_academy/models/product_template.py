from odoo import models, fields, api

class ProductTemplate(models.Model):
    _inherit = 'product.template'
    is_session_product = fields.Boolean(string='use as session product', help='Check this box to use this as a product for Session free' , default=False)

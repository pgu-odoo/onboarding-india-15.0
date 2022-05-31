from odoo import models , fields,api


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    is_session_product = fields.Boolean(string='use as session product' , help = 'check this box to use this as a product for session fee',default=False)

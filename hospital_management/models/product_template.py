# -*- coding: utf-8 -*-

from odoo import fields,models,api,_

class patient_template(models.Model):
    _inherit = "product.template"

    is_session_product = fields.Boolean(string='Use as Hospital Product',
                                         help='Check this box to use as a Product',default=False)
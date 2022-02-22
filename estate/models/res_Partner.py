from odoo import models,fields,api 

class ResPartner(models.Model):
    _inherit = 'res.partner'

    buyer_property_ids = fields.One2many('estate.property','buyer_id')
    is_buyer = fields.Boolean()



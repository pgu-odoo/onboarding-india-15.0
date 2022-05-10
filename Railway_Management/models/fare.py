from odoo import fields, models, api


class ModelName(models.Model):
    _name = 'railway.fare'
    _description = 'Journey Fare'

    name = fields.Many2one(comodel_name='railway.passenger',string='Passengers Name')
    ticket_charge = fields.Float(string='Journey_Fare')
    gst = fields.Float(string='GST')
    reservation_charge = fields.Float(string='Reservation_Fee')
    total = fields.Float(string='Total Fare')


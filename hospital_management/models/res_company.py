from odoo import models,,fields

class Company(models.Model):
    _inherit = 'res.company'

    def_patient_amount = fields.Float('Default Amount')
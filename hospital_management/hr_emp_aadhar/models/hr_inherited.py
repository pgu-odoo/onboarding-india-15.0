from odoo import fields,models

class ExtendEmployee(models.Model):
    _inherit = 'hr.employee'

    aadhar_no = fields.Char('Aadhar No.')
    pan = fields.Char('Pan No.')
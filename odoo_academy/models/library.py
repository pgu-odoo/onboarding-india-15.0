from odoo import models, fields, api


class Library(models.Model):
    _name = 'academy.library'
    _description = 'library model info'

    name = fields.Char(string='library Title', required=True)
    description = fields.Text(string='description library')

    level = fields.Selection(string='Level', selection=[(
        'beginner', 'Beginner'), ('intermediate', 'Intermediate'), ('advanced', 'Advanced')], copy=False)

    active = fields.Boolean(string='Active', default=True)

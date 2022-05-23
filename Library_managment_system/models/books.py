from numpy import require
from odoo import models, fields


class Books(models.Model):
    _name = 'library.books'
    _description = 'library management system'

    name = fields.Char(string='name', required=True)
    description = fields.Text(string='description')

    price = fields.Integer(string='price')
    category = fields.Selection(
        selection=[('fiction', 'Fiction',), ('action', 'Action')])
    isbn = fields.Integer()
    active = fields.Boolean(string='Active', default=True)

    level = fields.Selection(string='Level', selection=[(
        'beginner', 'Beginner'), ('intermediate', 'Intermediate'), ('advanced', 'Advanced')], copy=False)

from copy import copy
from email.policy import default
from odoo import models, fields, api


class Course(models.Model):
    _name = 'academy.course'
    _description = 'course info'

    name = fields.Char(string='Title', required=True)
    description = fields.Text(string='description')

    level = fields.Selection(string='Level', selection=[(
        'beginner', 'Beginner'), ('intermediate', 'Intermediate'), ('advanced', 'Advanced')], copy=False)

    active = fields.Boolean(string='Active', default=True)




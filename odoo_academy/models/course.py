
from odoo import models,fields,api


class Course(models.Model):

    _name = "course.academy"
    _description = "Course Info"
    
    name = fields.Char(string="Title",Required=True)
    description = fields.Text(string="Description")

    level = fields.Selection(string="Level",
    selection=[("Beginner","Beginner"),("Intermediate","Intermediate"),("Advanced","Advanced")],copy=False)

    active=fields.Boolean(string="Active", default=True)


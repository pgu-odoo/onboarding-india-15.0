
import string
from odoo import models,fields,api


class Course(models.Model):

    _name = "course.academy"
    _description = "Course Info"
    
    
    name = fields.Char(string="Title")
    description = fields.Text(string="Description")

    level = fields.Selection(string="Level",
    selection=[("Beginner","Beginner"),("Intermediate","Intermediate"),("Advanced","Advanced")],copy=False)

    active=fields.Boolean(string="Active", default=True)
    price = fields.Float(string="price")
    end_course_date = fields.Datetime(string='End Date')
    start_course_date = fields.Date(string='Start Date')
    


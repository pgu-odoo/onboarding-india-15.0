
from pickle import TRUE
import string
from odoo import models,fields,api


class Course(models.Model):

    _name = "course.academy"
    _description = "Course Info"
    
    
    name = fields.Char(string="Title",placeholder="Enter the course name ex. Maths")
    description = fields.Text(string="Description",help="Enter Description",readonly=False)

    level = fields.Selection(string="Level",
                selection = [("beginner","Beginner"),("intermediate","Intermediate"),("advanced","Advanced")],default='advanced')

    active=fields.Boolean(string="Active", default=True)

    price = fields.Float(string="price")
    end_course_date = fields.Datetime(string='End Date')
    start_course_date = fields.Date(string='Start Date')
    


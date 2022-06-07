
from odoo import models, fields, api

class Session(models.Model):
    _name = 'academy.session'
    _description = 'session info'

    course_id = fields.Many2one(comodel_name="course.academy", string="course",
                                    ondelete = "cascade", Required = True)


    name= fields.Char(string="Title", related= "course_id.name")                

    instructor_id = fields.Many2one(comodel_name="res.partner",string="Instructor") 

    student_ids = fields.Many2many(comodel_name="res.partner", string="Students")              
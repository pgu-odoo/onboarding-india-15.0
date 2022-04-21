# -*- coding: utf-8 -*-
from odoo import models, fields, api

class Session(models.Model):
	_name="institute.session"
	_description="session info"

	course_id= fields.Many2one(comodel_name='institute.course',
							   string='Course',
							   ondelete='cascade',
                               required= True)

	name = fields.Char(string='Title', related='course_id.name')

	instructor_id = fields.Many2one(comodel_name='res.partner', string='Instructor')

	student_ids = fields.Many2many(comodel_name='res.partner', string='Students')
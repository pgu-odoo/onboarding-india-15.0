from odoo import models, fields, api

class Course(models.Model):

	_name = 'academy.course'
	_discription = 'Course Info'
	

	description = fields.Text(string='Description')

	level = fields.Selection(string='Level', 
							 selection=[('beginner', 'Beginner'),
										('intermediate', 'Intermediate'),
										('advanced', 'Advanced')],
							 copy=False)
	
	active = fields.Boolean(string='Active', default=True)
	designation = fields.Char(string='Title', required=True)
	e_salary = fields.Char(string='salary', required=True)
	first_name = fields.Char(string='name', required=True)
	last_name = fields.Char(string='name', required=True)







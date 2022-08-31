#_*_ coding: utf-8 _*_

from odoo import models,fields,api

class Course(models.Model):

	_name = 'academy.course'
	_description = 'Course Info'

	name = fields.Char(string='Title', required=True)
	description = fields.Text(string='Level' , 
							  selection=[('beginner','Beginner'),
							  			 ('intermediate', 'Intermediate'),
							  			 ('advance','Advance')],
							  copy=False)
	active = fields.Boolean(string='Active' , default=True)


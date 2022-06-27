# -*- coding: utf-8 -*-

from odoo import model, field, api

class Course(models.model):

	_name = 'acadamy.course'
	_discription='course Info'

	name=fields.Char(string='Title', required=True)

	discription=fields.Text(string='Description')
	level=fields.Selection(string='level',

		       selection=[('beginner','Beginner'),
		                   ('intermediate','Intermediate'),
		                   ('advanced','Advanced')],
		                   copy=False)
	active=fields.Boolean(string='Active',default=True)


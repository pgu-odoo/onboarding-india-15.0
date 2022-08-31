#_*_ coding: utf-8 _*_

from odoo import models,fields,api

class book(models.Model):

	_name = 'library.book'
	_description = 'Book Info'

	name = fields.Char(string='Title', required=True)
	author = fields.Char(string='author name', required=True)
	editor = fields.Char(string='editor name')
	publisher = fields.Char(string='Publisher name', required=True)
	year_of_edition = fields.Char(string='Year of edition', required=True)
	ISBN= fields.Char(string='ISBN Code', required=True)
	genre= fields.Text(string='Level' , 
					   selection=[('fiction','Fiction'),
							  	  ('novel', 'Novel'),
							  	  ('fantasy','Fantasy'),
							  	  ('history','History'),
							  	  ('biopic', 'Biopic'),
							  	  ('fairytale','Fairytale'),
							  	  ('personal_development','Personal_Development')],
					   copy=False)
	active = fields.Boolean(string='Active' , default=True)

#_*_ coding: utf-8 _*_

from odoo import models,fields,api
from odoo.exceptions import ValidationError

class book(models.Model):

	_name = 'library.book'
	_description = 'Book Info'

	name = fields.Char(string='Title', required=True)
	note = fields.Text(string='Note')
	author = fields.Char(string='Author name', required=True)
	editor = fields.Char(string='Editor name')
	publisher = fields.Char(string='Publisher name', required=True)
	year_of_edition = fields.Char(string='Year of edition', required=True)
	genre= fields.Selection(string='Genre' , 
					   selection=[('fiction','Fiction'),
							  	  ('novel', 'Novel'),
							  	  ('fantasy','Fantasy'),
							  	  ('history','History'),
							  	  ('biopic', 'Biopic'),
							  	  ('fairytale','Fairytale'),
							  	  ('personal_development','Personal_Development')],
					   copy=False)
	active = fields.Boolean(string='Active' , default=True)

	isbn= fields.Char(string='ISBN Code' , required=True)

	@api.constrains('isbn')
	def _size_isbn(self):
		for record in self:
			if len(self.isbn) > 12:
				raise ValidationError('The length of ISBN code should must be of 13 ')

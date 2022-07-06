# -*- coding: utf-8 -*-

from odoo import models, fields, api

from odoo.exceptions import UserError, ValidationError

class Book(models.Model):

	_name = 'library.book'

	_description = "library book"

	name=fields.Char(string='Name',required=True)

	authors=fields.Char(string='Author name',required=True)

	editors=fields.Char(string='Editors Name', required=True)

	publishers=fields.Char(string='Publisher', required=True)

	year_of_edition=fields.Date(string='Year of Edition')

	number_isbn=fields.Char(string='ISBN No.',required=True)

	price=fields.Float(string="Price",required=True)

	note=fields.Text(string="Note")

	# @api.onchange('number_isbn')
	# def _check_isbn_length(self):
	# 	import pdb
	# 	pdb.set_trace()
	# 	# if len(self.number_isbn) > 0:
	# 	# 	if len(self.number_isbn) < 12:
	# 	# 		raise UserError('ISBN is not Correct')

	@api.constrains('number_isbn')
	def _isbn_size(self):
		for record in self:
			if len(self.number_isbn) < 12:
				raise ValidationError('ISBN Length is not Correct %s' % record.number_isbn)



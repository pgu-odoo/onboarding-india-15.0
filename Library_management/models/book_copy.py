# -*- coding: utf-8 -*-

from odoo import models, fields, api

class BookCopy(models.Model):
	_name='book.copy'
	_description='Book Copy Info'

	_inherits = {'library.book': 'book_id'}
	
	book_id=fields.Many2one(comodel_name='library.book',
		                        string='Book Id',
		                        ondelete='cascade',
		                        required=True)

	internel_ref=fields.Char(string='Reference Name',required=True)




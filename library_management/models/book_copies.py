# _*_coding : utf-8 _*_

from odoo import models,fields,api


class BookCopies(models.Model):
	_name = 'book.copies'

	_inherits = {'library.book': 'book_id'}

	rental_ids = fields.One2many(comodel_name='library.rental',
								 inverse_name='book_id',
								 string='Rental ids')
	internal_ref = fields.Char()

	# name = fields.Char(string='Title' , related='book_id.name')
	# note = fields.Text(string='Note' , related='book_id.note')
	# author = fields.Char(string='Author name', related='book_id.author')
	# editor = fields.Char(string='Editor name' ,related='book_id.editor')
	# publisher = fields.Char(string='Publisher name', related='book_id.publisher')
	# isbn= fields.Char(string='ISBN Code' , related='book_id.isbn')
	# customer_id = fields.Many2one(comodel_name='res.partner')
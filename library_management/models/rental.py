# _*_ coding: utf-8 _*_

from odoo import models,fields,api

class Rental(models.Model):

	_name = 'library.rental'
	_description = 'Rental info'

	book_id = fields.Many2one(comodel_name='library.book',
							 string='Book',
							 ondelete='cascade',
							 required=True)

	intref = fields.Integer(string='Internal Reference ID')

	name = fields.Char(string='Title' , related='book_id.name')

	customer_id = fields.Many2one(comodel_name='res.partner' , string='Customer')

	author = fields.Char(string='Author name', related='book_id.author')
	editor = fields.Char(string='Editor name' ,related='book_id.editor')
	publisher = fields.Char(string='Publisher name', related='book_id.publisher')
	isbn= fields.Char(string='ISBN Code' , related='book_id.isbn')
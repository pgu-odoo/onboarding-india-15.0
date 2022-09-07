# _*_ coding: utf-8 _*_

from odoo import models,fields,api

class Rental(models.Model):

	_name = 'library.rental'
	_description = 'Rental info'

	book_id = fields.Many2one(comodel_name='library.book',
							 string='Book',
							 ondelete='cascade',
							 required=True)

	name = fields.Char(string='Title' , related='book_id.name')

	customer_id = fields.Many2one(comodel_name='res.partner' , string='Customer')
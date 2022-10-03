## -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import  models, fields, api
from odoo.exceptions import UserError 


class Book(models.Model):

	_name = 'library.book' 
	_description = 'Book Info'

	name   = fields.Char(string = 'Tittle' , required=True)
	author = fields.Text(string = 'Author')
	editor = fields.Text(string = 'Editor')
	publisher = fields.Text(string = 'publisher')
	isnb = fields.Integer(string = 'ISNB Number')
	active = fields.Boolean(string = "Active")

	rental_ids = fields.One2many(comodel_name = 'library.rental' ,
								 inverse_name='book_id',
								 string = 'Rentals')

     

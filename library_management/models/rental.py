## -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import  models, fields, api


class Rental(models.Model):

	_name = 'library.rental' 
	_description = 'Rental Info'

	book_id = fields.Many2one(comodel_name="library.book",
								string="Book",
								ondelete = 'cascade',
								required = True)

	name =  fields.Char(string="Title" , related='book_id.name')
	
	customer_ids = fields.Many2many(comodel_name = 'res_partner' , string = 'Customers')





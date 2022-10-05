## -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import  models, fields, api

class SaleOrder(models.Model):

	_inherit = 'sale.order'

	book_id = fields.Many2one(comodel_name='library.rental',
								string ='Related Rental',
								ondelete = 'set null')

	customer_ids = fields.Many2many(string='Customers',
									related='book_id.customer_ids')

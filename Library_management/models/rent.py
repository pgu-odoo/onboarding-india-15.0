# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Rent(models.Model):
	_name="library.rent"
	_description="Rent Info"

	name=fields.Char(string='Title')

	customer_id=fields.Many2one(comodel_name='res.partner',
		                       string='Customer',
		                       required=True)

	book=fields.Many2one(comodel_name='book.copy',string='Book')



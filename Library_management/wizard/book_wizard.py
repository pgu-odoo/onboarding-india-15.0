# -*- coding: utf-8 -*-

from odoo import models, fields, api

class BookRent(models.TransientModel):

	_name='library.book.wizard'

	_description='wizard: Rented Book'

	rent_ids=fields.Many2many('library.rent',string="Rented Book", required=True)


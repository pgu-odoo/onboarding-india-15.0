# _*_ coding :  utf-8 _*_

from odoo import models, fields, api

class BookWizard(models.TransientModel):

	_name='library.book.wizard'
	_description='wizard: Rented Book'

	rental_ids=fields.Many2many(comodel_name='library.rental',string="Rented Book", required=True)

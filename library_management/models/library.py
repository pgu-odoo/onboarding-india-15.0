from odoo import models, fields, api

class management(models.Model):

	_name = 'library.management'
	_description = 'library books'
	

	name = fields.Char(string="author_name",required=True)
	description = fields.Text(string="book_description")
	category = fields.Selection(string="book_category",
								selection = [('management', 'Management'),
											('technology','Technology'),
											('mythology', 'Mythology')],
								copy=False)
	summary = fields.Char(string="book_summary", required=True)
	active = fields.Boolean(string="Active", default=True)
	


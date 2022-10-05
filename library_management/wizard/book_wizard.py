from odoo import api,fields ,models

class BookWizard(models.TransientModel):

	_name = 'library.book.Wizard'
	_description = 'Wizard Book'

	book_id = fields.Many2one(comodel_name="library.book",
								string="Book",
								ondelete = 'cascade')
	customer_ids = fields.Many2many(comodel_name = 'res_partner' , string = 'Customers')



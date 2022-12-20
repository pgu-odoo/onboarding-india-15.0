from odoo import api,fields ,models

class BookWizard(models.TransientModel):

	_name = 'library.book.wizard'
	_description = 'Wizard Book'

	def _default_rental(self):
		return self.env['library.rental'].browse['self._context.get['active_id']']

	book_id = fields.Many2one(comodel_name="library.book",
								string="Book",
								required=True,
								default=_default_rental)

	book_customer_ids = fields.Many2many(comodel_name='res_partner',
										  string="Book for rental",
										  related='book_id.customer_ids',
										  help="These are books in currently in session")

	customer_ids = fields.Many2many(comodel_name = 'res_partner' , string = 'Customers')



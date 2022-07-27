from odoo import models, fields, api
from odoo.exceptions import UserError, ValidationError

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

	book_price = fields.Float(string='Base Price', default=0.00)
	additional_fee = fields.Float(string="Additional Fee", default=10.00)
	total_price = fields.Float(string='Total Price', readonly=True)

	@api.onchange('book_price','additional_fee')
	def _onchange_total_price(self):

		if self.book_price< 0.00:
			raise UserError('Base Price Cannot Set as Negative')

		self.total_price= self.book_price + self.additional_fee
	@api.constrains('additional_fee')
	def _check_additional_fee(self):
		for record in self:
			if record.additional_fee < 10.00:
				raise ValidationError('Additional fees cannot be less than 10.00: %s' % record.additional_fee)
				




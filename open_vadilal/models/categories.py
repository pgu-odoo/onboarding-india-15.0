from odoo import models,fields,api
from odoo.exceptions import UserError,ValidationError

class Categories(models.Model):
	_name = 'vadilal.categories'
	_description = 'Categories Info'

	name = fields.Char(string='Categories',required=True)
	description = fields.Text(string='Description')
	level = fields.Selection(string='Level',
		                      selection=[('cone','Cone'),
		                                 ('candy','Candy'),
		                                 ('cake','Cake')],
		                       
		                       copy=False)

	active = fields.Boolean(string="active",default=True)

	wholesale_rate=fields.Float(string="Wholesale",default=0.00)
	retail_rate=fields.Float(string="Retail rate",default=0.00)
	total_rate=fields.Float(string="Total Rate",default=True)

	session_ids=fields.One2many(comodel_name='vadilal.session',
		inverse_name='categories_id',string="Sessions")

	@api.onchange('wholesale_rate','retail_rate')
	def _onchange_total_rate(self):

		if self.wholesale_rate < 0.00:
			raise UserError('Wholesale rate cannot be set as negative.')



		self.total_rate= self.wholesale_rate + self.retail_rate


	@api.constrains('retail_rate')

	def _check_retail_rate(self):

		for record in self:

			if record.retail_rate>10.0:

				raise ValidationError('retail rate cannot be less than 10.00: %s' % record.retail_rate)

				

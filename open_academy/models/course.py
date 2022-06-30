from odoo import models,fields,api
from odoo.exceptions import ValidationError, UserError

class Course(models.Model):

	_name = 'academy.course'
	_description = 'course Info'


	name = fields.Char(string='Course',required=True)
	description = fields.Text(string='description')
	level=fields.Selection(string='Level',
		                         selection=[('beginner','Beginner'),
		                                    ('intermidiate','Intermidiate'),
		                                    ('advanced','Advanced')],
		                          copy=False)

	active = fields.Boolean(string='active',default=True)

	base_price = fields.Float(string='Base price',default=0.00)

	additional_fee = fields.Float(string='Additional Fee',default=0.00)

	total_price=fields.Float(string='Total Price',default=True)

	session_ids=fields.One2many(comodel_name='academy.session',
		inverse_name="course_id",string="Sessions")

	@api.onchange('base_price','additional_fee')

	def _onchange_total_price(self):

		if self.base_price < 0.00:
			raise UserError('Base price cannot be set as negative.')



		self.total_price = self.base_price + self.additional_fee

	@api.constrains('additional_fee')

	def _check_additional_fee(self):

		for record in self:

			if record.additional_fee>10.0:

				raise ValidationError('Additional Fee must cannot be less than 10.00: %s' % record.additional_fee)

			
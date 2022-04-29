# -*-coding: utf-8 -*-
from odoo import models,fields,api
from odoo.exceptions import UserError,ValidationError
class Course(models.Model):

	_name='academy.course'
	_description='course Infod'
	name=fields.Char(string='Title',required=True)
	description=fields.Text(string='Description')
	level=fields.Selection(string='Level',selection=[('beginner','Beginner'),('intermediate','Intermediate'),('advanced','Advanced')],copy=False)
	active=fields.Boolean(string='Active',default=True)
	base_price=fields.Float(string='Base price',default=0.00)
	additional_fee=fields.Float(string='Additional fee',default=10.00)
	total_price=fields.Float(string='total price',readonly=True)
	@api.onchange('base_price','additional_fee')
	def _onchange_total_price(self):
		if self.base_price <0.00:
			raise UserError('base price cannot be set as negative')
		self.total_price=self.base_price+self.additional_fee
	@api.constrains('additional_fee')
	def _check_additional_Fee(self):
		for record in self:
			if record.additional_fee <10.00:
				raise ValidationError('Additional Fees cannot be less than 10.00:%s' % record.additional_fee)


		
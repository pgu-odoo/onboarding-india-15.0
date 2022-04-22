# -*- coding: utf-8 -*-
from odoo import models,fields,api,_
from odoo.exceptions import UserError,ValidationError


class Course(models.Model):

	_name='academy.course'
	_description='Course info'


	# Fields of odoo
	# Monetory is use for calculation
	# Integer ,Float,Boolean,Selection,Text,Char,Html,Date,Datetime

	name =fields.Char(string='Title',required=True) #required True bacause we always have a title
	description=fields.Text(string='Description')

	level=fields.Selection(string='Level',selection=[('beginner','Beginner'),('intermediate','Intermediate'),('advanced','Advanced')],copy=False,default='beginner')

	active =fields.Boolean(string='Active',default=True)

	base_price=fields.Float(string="Base Price",default=0.00)
	additional_fee=fields.Float(string="Additional_fee",default=10.00)
	total_price=fields.Float(string="Total_Price")


	@api.onchange('base_price','additional_fee')
	def _onchange_total_price(self):
		if self.base_price<0.00:
			raise UserError('base price cannot be set as nagative')

		self.total_price=self.base_price+self.additional_fee



	@api.onchange('additional_fee')
	def _check_additional_fee(self):
		for record in self:
			if record.additional_fee<10.00:
				raise ValidationError('additional_fee cannot be less than 10: %s'%record.additional_fee)
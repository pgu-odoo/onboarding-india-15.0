# -*-coding: utf-8 -*-
from odoo import models,fields,api,_
from odoo.exceptions import UserError,ValidationError


class Course(models.Model):
	_name='academy.course'
	_description='course Infod'

	name=fields.Char(string='Title',required=True,size=4)
	description=fields.Text(string='Description')
	gender = fields.Selection([('male','Male'),('female','Female'),('other','Other')],help='Choose a gender', copy=False)
	country_code=fields.Integer(string="enter your country code",required=True)
	dhtml=fields.Html(string="html data",required=True)
	bina=fields.Binary(string="binary data",required=True)
	level=fields.Selection(string='Level',selection=[('beginner','Beginner'),('intermediate','Intermediate'),('advanced','Advanced')],copy=False)
	active=fields.Boolean(string='Active')
	base_price=fields.Float(string='Base price',default=True,digits=(4,3))
	additional_fee=fields.Float(string='Additional fee',default=10.00)
	total_price=fields.Float(string='total price',readonly=True)
	passw=fields.Char(string="pwd",size=6)
	session_ids=fields.One2many(comodel_name='academy.session',inverse_name='course_id',string='Sessions')

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


		

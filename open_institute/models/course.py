# -*- coding: utf-8 -*-


from odoo import models, fields, api

class Course(models.Model):

	_name = 'institute.course'
	_description = 'open institute module'
	
	name = fields.Char(string="Title", required=True)
	description= fields.Text(string='Description')

	level = fields.Selection(string='Level',
							  selection= [('beginner', 'Beginner'),
							  			  ('intermediate', 'Intermediate'),
							  			   ('advanced', 'Advanced')],
							  copy = False)

	active = fields.Boolean(string='Active', default=True)

	base_price = fields.Float(string='Base Price', default=0.00)

	additional_price = fields.Float(string='Additional Price', default=0.00)

	total_price = fields.Float(string='Total Price', readonly=True)

	@api.onchange('base_price','additional_price')
	def _onchange_total_price(self):
		 self.total_price = self.base_price + self.additional_price
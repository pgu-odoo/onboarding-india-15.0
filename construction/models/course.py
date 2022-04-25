# -*- coding: utf-8 -*-
from odoo import models,fields,api,_
from odoo.exceptions import UserError,ValidationError


class Course(models.Model):

	_name='academy.course'
	_description='Course info'


	# Fields of odoo are  Monetory is use for calculation,Integer ,Float,Boolean,Selection,Text,Char,Html,Date,Datetime

	name =fields.Char(string='Title',required=True) #required True bacause we always have a title
	description=fields.Text(string='Description')

	level=fields.Selection(string='Level',selection=[('beginner','Beginner'),('intermediate','Intermediate'),('advanced','Advanced')],copy=False,default='beginner')

	active =fields.Boolean(string='Active',default=True)

	base_price=fields.Float(string="Base Price",default=0.00)
	additional_fee=fields.Float(string="Additional_fee",default=10.00)
	total_price=fields.Float(string="Total_Price",compute='_compute_total_price')

	subject = fields.Many2one(comodel_name='subject.details',string="Subject")
	add_subject = fields.One2many('subject.details','details_id',string="Subject Options")


	# @api.onchange('base_price','additional_fee')  # invoke when we  change in  "additional_fee"  and "base_price" and we can changes in total_price
	# def _onchange_total_price(self):
	# 	print("ssssssssssssssssssssss",self.base_price)
	# 	if self.base_price<0.00:
	# 		raise UserError('base price cannot be set as nagative')

	# 	self.total_price=self.base_price+self.additional_fee

	@api.depends('base_price','additional_fee') # invoke when we  change in  "additional_fee"  and "base_price" and we can't changes in total_price
	def _compute_total_price(self):
		print("base_price------------------>",self.base_price)
		if self.base_price<0.00:
			raise UserError('base price cannot be set as nagative')

		self.total_price=self.base_price+self.additional_fee



	@api.onchange('additional_fee') # invoke when we  change in  "additional_fee" 
	def _check_additional_fee(self):
		for record in self:
			print('self ------------------>',record)
			if record.additional_fee<10.00:
				raise ValidationError('additional_fee cannot be less than 10: %s'%record.additional_fee)

	@api.model
	def create(self,vals): # invoke when we click on create+save button 
		print("create  method------------------>",vals)
		if vals.get('name') == 'meet':
			vals['name'] = 'Riddhi'
		res = super(Course,self).create(vals)
		return res
		# super(classname,self).craete(other parameer which given in function)

	
	def write(self,vals):  #no decorators needed for  write method  invoke when we click on Edit+save button
		print("write method------------------>",vals)
		if vals.get('name') == 'meet':
			vals['name'] = 'Meet'
		res = super(Course,self).write(vals)
		return res

	@api.constrains('description')
	def check_description(self):
		for rec in self:
			note=self.env['academy.course'].search([('description', '=', rec.description)])
			if note:
				raise ValidationError("description is  %s already exists",rec.description)




	@api.onchange('base_price','additional_fee')  # invoke when we  change in  "additional_fee"  and "base_price" and we can changes in total_price
	def _onchange_total_price(self):
		browse_method=self.env['academy.course'].browse([15,14,1])
		
		print('-------------------------------------->>>',browse_method) #browse_method=academy.course(15, 14, 1)

		for i in browse_method: # i=academy.course(1,) ,i=academy.course(15,),i=academy.course(14,) 
			print(i.additional_fee)  

		# search_method=self.env['academy.course'].search([('partner_id', '=', seller.id)])
        




	


class SubjectDetails(models.Model):

	_name = 'subject.details'
	_description = 'Subject Details'
	_rec_name = "subject"

	subject = fields.Char('Subject')
	book = fields.Char('Book Name')
	author = fields.Char("Author")
	details_id = fields.Many2one('academy.course',string="details")

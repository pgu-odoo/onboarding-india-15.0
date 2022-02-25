# -*- coding: utf-8 -*-
from odoo import models, fields, api, _
from dateutil.relativedelta import relativedelta
from datetime import date, datetime
from odoo.exceptions import UserError, ValidationError

#property class 
class EstateProperty(models.Model):
	_name = 'estate.property'
	_description = 'Estate property'
	_order = 'id desc'


	name = fields.Char(string='Title', required=True)
	description = fields.Text(string='Description')
	postcode = fields.Char(string='Postcode')
	# lambda function use for take the any data from without declaring the function body here I use this for take date and time from
	date_availability = fields.Date(string='Date Availablity From', copy=False, default=lambda self: fields.Date.today() + relativedelta(months=+3))
	expected_price = fields.Float(string='Expected Price', help='What is your expected price of the property?')
	bedrooms = fields.Integer(string=_('No. of Bedrooms'), default=2)
	living_area = fields.Integer(string='Living Area (sqm)')
	facades = fields.Integer(string='Facades')
	garage = fields.Boolean(string='Garage')
	garden = fields.Boolean(string='Garden')
	garden_area = fields.Integer(string='Garden Area (sqm)', help='How much Area does your Garden contain? (Give Approx. Measurement)')
	active = fields.Boolean(string='Active', default=True)
	is_sold = fields.Boolean(default=False, invisible=True)
	is_cancelled = fields.Boolean(default=False, invisible=True)

	#selection fields
	garden_orientation = fields.Selection(string='Garden Orientation', 
											selection = [	('north', 'North'),
															('east', 'East'),
															('south', 'South'),
															('west', 'West')
														]
											)
	
	#relational fields
	property_type_id = fields.Many2one('estate.property.type', ondelete='restrict')
	salesman_id = fields.Many2one('res.users', default=lambda self : self.env.user, copy=False)
	buyer_id = fields.Many2one('res.partner',compute='_compute_sold')
	property_tag_ids = fields.Many2many('estate.property.tag','property_tag_rel','tag_ids','property_tag_ids')
	property_offer_ids = fields.One2many('estate.property.offer','property_id')

	#compute fields                                                                                                  
	total_area = fields.Integer(string='Total Area (sqm)', readonly=True,compute='_compute_total_area')
	date_deadline = fields.Date(string='Date Availability To', copy=False)
	validity = fields.Integer(string='Days Available', compute='_compute_validity', inverse='_inverse_validity')
	best_price = fields.Float(compute='_compute_best_price')
	selling_price = fields.Float(string='Selling Price', readonly=True, copy=False, compute='_compute_sold')
	state = fields.Selection(string='Status',
								selection = [	('new','New'),
												('offer_received', 'Offer Received'),
												('offer_accepted', 'Offer Accepted'),
												('sold', 'Sold'),
												('cancelled','cancelled')
											],
								copy=False, 
								default='new',
								compute='_compute_offer_received', store=True)

	_sql_constraints = [
						('check_expected_price', 'CHECK(expected_price > 0)','Expected Price must be Positive')
					]

	@api.ondelete(at_uninstall=False)
	def _def_ondelete(self):
		if (self.state != 'new' and self.state != 'cancelled'):
			raise ValidationError(_('Property Can\'t be deleted if it is not in new or cancelled state!!'))

	@api.depends('property_offer_ids.status') 
	def _compute_sold(self):
		for record in self:
			sold_price = 0
			buyer = None

			for offer in record.property_offer_ids:
				if offer.status == 'accepted':
					sold_price = offer.price
					buyer = offer.partner_id
					# record.state = 'sold'
			record.selling_price = sold_price
			record.buyer_id = buyer	
				
	@api.depends('property_offer_ids','is_sold','is_cancelled')
	def _compute_offer_received(self):
		for record in self:
			if record.is_sold == True:
				record.state = 'sold'
			elif record.is_cancelled == True:
				record.state = 'cancelled'
			else:
				if (len(record.property_offer_ids) > 0):
					record.state = 'offer_received'
					for offer in record.property_offer_ids :
						if  offer.status == 'accepted' and record.state != 'sold':
							record.state = 'offer_accepted'
				else:
					record.state = 'new'

	@api.depends('property_offer_ids')
	def _compute_best_price(self):
		for record in self:
			record.best_price = max(record.property_offer_ids.mapped('price') or [0])

	
	@api.onchange('garden')
	def _onchange_garden(self):
		if self.garden == True:
			self.garden_area = 10
			self.garden_orientation = 'north'
		else:
			self.garden_area = 0
			self.garden_orientation = None

	@api.depends('living_area','garden_area')
	def _compute_total_area(self):
		for record in self:
			record.total_area = record.living_area + record.garden_area

	@api.onchange('date_availability')
	def _onchange_date_availabilty_from(self):
		self.date_deadline = self.date_availability + relativedelta(months=+1)
	
	@api.depends('date_availability','date_deadline')
	def _compute_validity(self):
		for record in self:
			from_date = datetime.strptime(str(record.date_availability), '%Y-%m-%d')
			to_date = datetime.strptime(str(record.date_deadline), '%Y-%m-%d')
			daysDiff = str((to_date-from_date).days)
			record.validity = daysDiff

	@api.depends('validity')
	def _inverse_validity(self):
		for record in self:
			record.date_deadline = record.date_availability + relativedelta(days =+ record.validity)
                                                                                         
	@api.constrains('garden_area') 
	def _constrains(self):
		for record in self:
			if self.garden_area > self.living_area :
				raise ValidationError('Garden Area can\'t be bigger than Living Area.')
	
	def action_sold(self):
		for record in self:
			if record.state == "cancelled":
				raise UserError("Cancelled Property can\'t be Sold!!")
			record.is_sold = True

	def action_cancel(self):
		for record in self:
			if record.state == "sold":
				raise UserError("Sold Property Can\'t be Cancelled")
			record.is_cancelled = True
	
# Property Type Class
class EstatePropertyType(models.Model):
	_name = 'estate.property.type'
	_description = 'Estate Property Type'
	_order = 'sequence, name'


	name = fields.Char(required=True)
	sequence = fields.Integer('Sequence', default=1, help='Used to order stages. lower is better')

	#relational fields
	property_ids = fields.One2many('estate.property','property_type_id')
	offer_ids = fields.One2many('estate.property.offer','property_type_id')
	offer_count = fields.Integer(compute="_compute_offer_count")

	_sql_constraints = [
						('unique_name','UNIQUE(name)','Type name must be Unique!!')
					]

	@api.depends('offer_ids')
	def _compute_offer_count(self):
		for record in self:
			record.offer_count = len(record.offer_ids)



#Property Tags Class
class PropertyTags(models.Model):
	_name= 'estate.property.tag'
	_description = 'Tags to be given to differnt properties'
	_order = 'name'

	name = fields.Char(required=True)
	color = fields.Integer()

	#relational fields
	tag_ids = fields.Many2many('estate.property','property_tag_rel','property_tag_ids','tag_ids')

	_sql_constraints = [
						('unique_name','UNIQUE(name)','Tag name must be Unique!!')
					]


#Property Offer Class
class EstatePropertyOffer(models.Model):
	_name='estate.property.offer'
	_description='Estate Property'
	_order = "price desc"

	price = fields.Float(required=True)

	#selection fields
	status = fields.Selection(string='Status',
								selection=[('accepted','Accepted'),
											('refused','Refused')
										],
								copy=False)
	
	#relations fields
	partner_id = fields.Many2one('res.partner')
	property_id = fields.Many2one('estate.property')
	property_type_id = fields.Many2one(string="Offers", related="property_id.property_type_id", store=True)

	_sql_constraints = [
						('check_offer_price','CHECK(price > 0)','Offer Price must be Positive')
					]
	
	# @api.model
	# def create(self,vals):
	# 	best = self.env['estate.property'].browse('best_offer')


	def action_accept_offer(self):
		for record in self:
			record.status = "accepted"
		
	def action_refuse_offer(self):
		for record in self:
			record.status = "refused"









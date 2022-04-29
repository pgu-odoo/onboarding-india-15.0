# -*- coding: utf-8 -*-
from odoo import models, fields, api
from datetime import timedelta

class Estate_Property(models.Model):
	_name = "estate.property"
	_description = "A package for complete Real Estate Solutions"

	property_type_id = fields.Many2one('estate.property.type', string="Property Type")
	salesperson = fields.Many2one('res.users', string='Salesperson', index=True, default=lambda self: self.env.user)
	buyer = fields.Many2one('res.partner', string="Buyer")
	tags_ids = fields.Many2many('estate.property.tag', string="Tags")
	offers_ids = fields.One2many("real.estate.property.offer", "partner_id", string="Offers")
	name = fields.Char(string="Title", required=True)
	active = fields.Boolean(string="Active")
	description = fields.Text(string="Description" )
	postcode = fields.Char(string="PostCode")
	date_availability = fields.Date(string="Available From", copy=False, default=lambda self:fields.Datetime.now() + timedelta(days=+90))
	expected_price = fields.Float(string="Expected Price",required=True)
	selling_price = fields.Float(string="Selling Price", copy=False, readonly=True)
	bedrooms = fields.Integer(string="Bedrooms", default=2)
	living_area = fields.Integer(string="Living Area(sqm)")
	facades = fields.Integer(string="Facade")
	garage = fields.Boolean(string="Garage")
	garden = fields.Boolean(string="Garden")
	garden_area = fields.Integer(string="Garden Area(sqm)")
	garden_orientation = fields.Selection(
		string='Garden Orientation',
		selection=[('north', 'North'), ('south', 'South'), ('east', 'East'), ('west', 'West')])
	state = fields.Selection(string="State", selection=[('new', 'New'), ('offer recieved', 'Offer Recieved'), ('offer accepted', 'Offer Accepted'), ('sold', 'Sold'), ('canceled', 'Canceled')], required=True, copy=False, default="new")
	total_area = fields.Float(compute="_compute_total_area", store=True)

	@api.depends('living_area', 'garden_area')
	def _compute_total_area(self):
		for x in self:
			x.total_area = x.living_area + x.garden_area

	@api.onchange('garden')
	def _set_default_orientation(self):
		if self.garden:
			self.garden_orientation = 'north'
			self.garden_area = 10
		else:
			self.garden_area = 0.00
			self.garden_orientation = ""
	
	# def action_set_property_sold(self):
	# 	if 	self.sold:
	# 		self.cancel 

	# def action_set_property_sold(self):
	# 	if 	self.sold:
	# 		self.cancel
			

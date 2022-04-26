# -*- coding: utf-8 -*-
from odoo import models, fields

class Estate_Property(models.Model):
	_name = "estate.property"
	_description = "A package for complete Real Estate Solutions"

	name = fields.Char(string="Real Estate Properties", required=True)
	description = fields.Text(string="Description" )
	postcode = fields.Char(string="Post Code")
	date_availability = fields.Date(string="Date") 
	expected_price = fields.Float(string="Expected Price",required=True)
	selling_price = fields.Float(string="Sellin Price")
	bedrooms = fields.Integer(string="Bedrooms")
	living_area = fields.Integer(string="Living area")
	facades = fields.Integer(string="facade")
	garage = fields.Boolean(string="Garage")
	garden = fields.Boolean(string="garden")
	garden_area = fields.Integer(string="garden_area")
	garden_orientation = fields.Selection(
		string='Type',
		selection=[('north', 'North'), ('south', 'South'), ('east', 'East'), ('west', 'West')])

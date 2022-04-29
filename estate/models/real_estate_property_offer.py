# -*- coding: utf-8 -*-
from odoo import models, fields, api

class RealEstatePropertyOffer(models.Model):
	_name = "real.estate.property.offer"

	price = fields.Float(string="Price")
	status = fields.Selection(string="Status",
		selection=[('accepted', 'Accepted'),('recieved', 'Recieved')], copy=False)
	partner_id = fields.Many2one('estate.property', string="Partner id", required=True)
	property_id = fields.Many2one('estate.property', string="Property id", required=True)

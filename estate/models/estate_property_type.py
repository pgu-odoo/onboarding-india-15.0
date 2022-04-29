# -*- coding: utf-8 -*-
from odoo import models, fields, api

class EstatePropertyType(models.Model):
	_name = "estate.property.type"

	name = fields.Char(string="Property Type", required=True)
	

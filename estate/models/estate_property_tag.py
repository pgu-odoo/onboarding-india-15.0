# -*- coding: utf-8 -*-
from odoo import models, fields, api

class EstatePropertyTag(models.Model):
	_name = "estate.property.tag"

	name = fields.Char(string="Property Tag")
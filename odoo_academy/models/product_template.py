# -*- coding: utf-8 -*-

from odoo import models, fields, api

class ProductTemplate(models.Model):
	_inherit='product.template'

	is_session_product=fields.Boolean(string="Use as Session Product",
		                               help="Check this box is use as a product for session fee" 
		                               ,default=False)
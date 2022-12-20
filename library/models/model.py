## -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import  models, fields, api

class Library(models.Model):
	_name = "schhol.library"
	partner_id = fields.Many2one('res_partner',string='customer')

class LibraryOrder(models.Model):
	_name = "schhol.library order"



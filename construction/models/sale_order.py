# -*- coding: utf-8 -*-
from odoo import models,fields,api,_


class Saleorder(models.Model):

	_inherit="sale.order"  # sale.order is technical name for sale oder 

	title12 =fields.Char(string='Title')
	

	
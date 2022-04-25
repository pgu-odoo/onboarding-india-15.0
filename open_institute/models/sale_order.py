# -*-coding: utf-8-*-
from odoo import models, fields, api

class SaleOrder(models.Model):
	_inherit='sale.order'
session_ids = fields.Many2many(comodel_name='institute.session',string='Related session',ondelete='set null')
instructor_id = fields.Many2many(string='Session Instructor',related='session_ids.instructor_id')
student_ids = fields.Many2many(string='Students',related='session_ids.student_ids')

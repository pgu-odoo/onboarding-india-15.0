# _*_  coding:utf-8 _*_

from odoo import models, fields , api

class BookOrder(models.Model):
	_inherit = 'sale.order'

	session_id = fields.Many2one(comodel_name='library.session',
								string='related session',
								ondelete='set null')
	instructor_id = fields.Many2one(string='session instructor')
	student_ids = fields.Many2many(string='students')


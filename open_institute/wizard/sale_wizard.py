# -*- coding:utf-8 -*-
from odoo import models, fields, api

class WizardSale(models.TransientModel):
	_name='institute.sale.wizard'
	_description='Wizard: Quick sale order for your institue'

	def _default_session(self):
		return self.env['institue.session'].browse(self.context.get('active_id'))

	session_ids = fields.Many2one(comodel_name="institue.session",string="Session", required=True, default=_default_session)

	student_ids = fields.Many2many(comodel_name='res.partner', string="Students for sale order")
	
	session_student_ids = fields.Many2one(comodel_name='res.partner', string="Students currently in session", related='session_ids.student_ids', help='These are students currently in sesssions')

	def create_sale_order(self):
		session_product_id=self.env['product.product'].search([('is_session_product','=','True')], limit=1)
		if session_product_id:
			for student in self.student_ids:
				order_id=self.env['sale.order'].create({
					'partner_id': student.id,
					'session_id': self.session_ids.id,
					'order_line': [(0,0,{'product_id': session_product_id, 'price_unit': self.session_ids.total_price})]
					})

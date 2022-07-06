# -*- coding: utf-8 -*-

from odoo import models, fields, api

class ProductTemplate(models.TransientModel):

	_name='acadamy.sale.wizard'
	_decription='wizard: Quick sale order for Session Students'

	def _default_session(self):
		return self.env['acadamy.session'].browse(self._context.get('active_id'))

	session_id=fields.Many2many('acadamy.session',
		                         string='Session',
		                         required=True,
		                         default=_default_session)

	session_student_ids=fields.Many2one(string='Students in Current Session',
		                                  related='session_id.student_id',
		                                  help='These are the Student Current in the Session')

	student_ids=fields.Many2many('res.partner',
		                          string='Students for sale order')

	def create_sale_order(self):
		session_product_id=self.env['product.product'].search([('is_session_product','=',True)],limit=1)
		if session_product_id:
			for student in self.student_ids:
				order_id=self.env['sale_order'].create({
					"partner_id" : student.id,
					"session_id" : self.session_id.id,
					"order_line" : [(0,0,{'product_id':session_product_id.id,'price_unit': self.session_id.total_price})]
					})
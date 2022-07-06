#-*- coding:utf-8 -*-

from odoo import http

class AvailableBook(http.Controller):
	@http.route('/book',auth='public',website=True)
	def available_book(self, **kw):
		book=http.request.env['library.book'].search([])
		return http.request.render('Library_management.book_website',{'book':book,})



# -*- coding: utf-8 -*-

from odoo import http


class Library(http.Controller):

	@http.route('/library/' , auth='public' , website=True)
	def index(self,**kw):
		return "hello world"

	@http.route('/library/books/' ,  auth='public' , website=True)
	def index(self,**kw):
		books = http.request.env['library.book'].search([])
		return http.request.render('odoo_library.book_website' , {
			'books': books,})
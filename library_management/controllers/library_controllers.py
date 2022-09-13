# _*_ coding:utf-8 _*_

from odoo import http


class Library(http.Controller):
	@http.route('/library/' , auth='public' , website=True)
	def index(self, **kw):
		return "Welcome to the Library"

	@http.route('/library/books/' , auth='public' , website=True)
	def books (self, **kw):
		books = http.request.env['library.book'].search([])
		return http.request.render('library_management.book_website' , {
			'books': books,
		})
 
	@http.route('/library/<model("library.rental"):rental>/' , auth='public' , website=True)
	def rental(self, rental):
		return http.request.render('library_management.rental_website' , {
			'rental' : rental,
		})
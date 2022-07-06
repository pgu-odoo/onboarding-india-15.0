#-*- coding:utf-8 -*-

from odoo import http

class Acadamy(http.Controller): 
	@http.route('/acadamy', auth='public', website=True)
	def index(self,**kw):
		return "Hello, word"

	@http.route('/acadamy/courses/',auth='public', website=True)
	def course(self, **kw):
		courses=http.request.env['acadamy.course'].search([])
		print("===================", courses)
		return http.request.render('odoo_academy.course_website', {
			'courses': courses,
			})

	@http.route('/acadamy<model("acadamy.session"):session>/', auth='public', website=True)
	def session(self, session):
		return http.request.render('odoo_acadamy.session_website',
			{
			'session':session,
			})
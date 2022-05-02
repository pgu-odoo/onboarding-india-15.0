from odoo import http
from odoo.http import request


class CourseController(http.Controller):

	@http.route('/Course_detail/subject/',website=True,auth='public') #three type of auth='public' (page is access by anyone),auth='user'(page is access by login user ),auth='non'

	def Course_detail(self,**kw):
		#return "hello odoo" 
		coursename=request.env['academy.course'].sudo().search([])  #sudo() is use for bypass all accessrule

		print('coursename---------',coursename)

		return request.render("construction.course_available",{
			'coursename':coursename
		})		#modulename.template_id
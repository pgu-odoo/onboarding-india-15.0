from odoo import models, fields, api

class session(models.Model):
	_name = 'library.session'
	_description = 'Session Info'

	book_id = fields.Many2one(comodel_name='library.management', string="book", ondelete="cascade", required=True)

	name = fields.Char(string='Title', related='book_id.name')
	
	isbn = fields.Char(string='ISBN')

	student_ids = fields.Many2many(comodel_name='res.partner', string='students')
	

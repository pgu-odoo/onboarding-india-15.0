from odoo import models, fields, api
from datetime import timedelta

class session(models.Model):
	_name = 'library.session'
	_description = 'Session Info'

	book_id = fields.Many2one(comodel_name='library.management', string="book", ondelete="cascade", required=True)

	name = fields.Char(string='Title', related='book_id.name')
	
	isbn = fields.Char(string='ISBN')

	student_ids = fields.Many2many(comodel_name='res.partner', string='students')

	start_date = fields.Date(string='start date',
							 default=fields.Date.today)
	duration = fields.Integer(string='session days', default=1)

	end_date = fields.Date(string="End Date", compute="_compute_end_date",
							inverse="_inverse_end_date",
							store=True)
	@api.depends('start_date', 'duration')
	def _compute_end_date(self):
		for record in self:
			if not (record.start_date and record.duration):
				record.end_date = record.start_date
			else:
				duration = timedelta(days=record.duration)
				record.end_date = record.start_date + duration

	def _inverse_end_date(self):
		for record in self:
			if record.start_date and record.end_date:
				record.duration = (record.end_date - record.start_date).days + 1
			else:
				continue








	

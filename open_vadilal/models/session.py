from odoo import models,fields,api
from datetime import timedelta

class Session(models.Model):
	_name='vadilal.session'
	_description='vadilal Info'


	categories_id=fields.Many2one(comodel_name='vadilal.categories',
		string='categories',
		ondelete='cascade',
		required=True)

	name=fields.Char(name='Title', related='categories_id.name')
	instructor_id=fields.Many2one(comodel_name='res.partner', string='Instructor')
	student_ids=fields.Many2many(comodel_name='res.partner',string='Students')

	start_date=fields.Date(string='Start Date', default=fields.Date.today)

	duration=fields.Integer(string='Session Days',default=1)

	end_date=fields.Date(string="end_date",
		compute="_compute_end_date",
		inverse="_inverse_end_date",
		store=True)

	@api.depends('start_date','duration')
	def _compute_end_date(self):
		for record in (self):
			if not(record.start_date and record.duration):
				record.end_date=record.start_date

			else:
				duration=timedelta(days=record.duration)
				record.end_date=record.start_date + duration

	def _inverse_end_date(self):
		for record in (self):
			if record.start_date and record.end_date:
				record.duration=(record.end_date-record.start_date).days+1
			else:
				continue
	
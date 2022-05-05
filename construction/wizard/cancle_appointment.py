# -*- coding: utf-8 -*-
from odoo import models,fields,api,_



class CancleLectureWizard(models.TransientModel):

	_name = 'create.appointment.wizard'
	_description = 'create appointment Wizard'
	

		
	course_name = fields.Many2one('academy.course',string="course name")	# id = fields.Many2one('relational.object.name',string='')
	

	def action_create_appointment(self):
		print('button click ')
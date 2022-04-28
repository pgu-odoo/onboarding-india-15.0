# -*- coding: utf-8 -*-
from odoo import models,fields,api,_



class CancleAppointmentWizard(models.TransientModel):

	_name = 'cancle.appointment.wizard'
	_description = 'Cancle Appointment Wizard'
	_rec_name = "subject"

	
	appointment_id = fields.Many2one('academy.course',string="details")	# id = fields.Many2one('relational.object.name',string='')

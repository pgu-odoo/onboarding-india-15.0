# -*- coding: utf-8 -*-
from odoo import models,fields,api,_



class SubjectDetails(models.Model):

	_name = 'subject.details'
	_description = 'Subject Details'
	_rec_name = "subject"



	subject = fields.Char('Subject')


	book = fields.Char('Book Name')
	
	author = fields.Char("Author")
	details_id = fields.Many2one('academy.course',string="details")	# id = fields.Many2one('relational.object.name',string='')
	

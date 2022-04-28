# -*- coding: utf-8 -*-
# from odoo import models,fields,api,_



# class SubjectDetails(models.Model):

# 	_name = 'subject.details'
# 	_description = 'Subject Details'
# 	_rec_name = "subject"


# 	subject = fields.Char('Subject')
	

# 	_inherits = {'academy.course': 'related_subject'} # {'which model we have to inherits':'field which we add in this model '}

# 	book = fields.Char('Book Name')
# 	author = fields.Char("Author")
# 	details_id = fields.Many2one('academy.course',string="details")	# id = fields.Many2one('relational.object.name',string='')
# 	related_subject = fields.Char('related_subject')

# -*- coding: utf-8 -*-
from odoo import models,fields,api,_
from odoo.exceptions import UserError,ValidationError
from datetime import timedelta



class HospitalPatient(models.Model):
	_name='hospital.patient'
	_description='for hospital patient'

	name=fields.Char(string='Name', required=True)
	age=fields.Char(string='Age')

	gender=fields.Selection([('male','Male'),('female','Female'),('other','Other')], required=True , default='male')


	description=fields.Text(string='Description')	
# -*- coding: utf-8 -*-
import string
from odoo import api, fields, models


class HospitalDoctors(models.Model):
    _name = "hospital.doctors"
    _description = "hospital Doctors"

    name = fields.Char(string='Name', required=True)
    age = fields.Integer(string='Age')
    
    gender = fields.Selection(string="Gender",selection=[
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'other'),
    ], required=True, default='other')
    
    note = fields.Text(string='Description')
    

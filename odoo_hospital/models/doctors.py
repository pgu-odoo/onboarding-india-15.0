# -*- coding: utf-8 -*-
from odoo import api, fields, models


class HospitalDoctors(models.Model):
    _name = "hospital.doctors"
    _description = "hospital Doctors"

    name = fields.Char(string='Name', required=True, translate=True)
    age = fields.Integer(string='Age', required=True, translate=True)
    include_initial_balance = fields.Boolean(string="Bring Accounts Balance Forward", help="Used in reports to know if we should consider journal items from the beginning of time instead of from the fiscal year only. Account types that should be reset to zero at each new fiscal year (like expenses, revenue..) should not have this option set.")
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'other'),
    ], required=True, default='other')
    
    note = fields.Text(string='Description')
    

# -*- coding: utf-8 -*-
from atexit import register
from odoo import api, fields, models
from odoo.exceptions import UserError, ValidationError


class HospitalPatients(models.Model):
    _name = "hospital.patients" #its create patients table with below attributes
    _description = "hospital patients"

    name = fields.Char(string='Name', required=True)
    age = fields.Integer(string='Age')
    gender = fields.Selection(string="Gender",selection=[  # selection= is required when we want access key(male,female,other) in xml file
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'other'),
    ], default='other')
    
    description = fields.Text(string='Description')

    active= fields.Boolean(string='Active',default=True)
    admit_fee= fields.Float(string='Registration Fee',default=0.0)
    additional_fee= fields.Float(string='Additional Fee',default=100.0)
    total_fee= fields.Integer(string='Total Fee',readonly=True)

    # @api.onchange('admit_fee','additional_fee')
    # def _onchange_total_fee(self):
    #     if self.admit_fee<0:
    #         raise UserError('Registration Fee must be greater than 0')

    #     self.total_fee=self.admit_fee+self.additional_fee

    # @api.constrains('additional_fee')
    # def _check_additional_fee(self):  #its will check for all records
    #         for record in self:
    #             if self.additional_fee<100.0:
    #                 raise ValidationError("Additional Fee should be greater than 10.0,your enter Additional Fee is",record.additional_fee)

# -*- coding: utf-8 -*-
# from atexit import register
from odoo import api, fields, models
from odoo.exceptions import UserError, ValidationError


class HospitalPatients(models.Model):
    _name = "hospital.patients" #its create patients table with below Columns name
    _description = "hospital patients"
    _inherit = ['mail.thread','mail.activity.mixin'] #inherit mail models for chatter to form view in patient

    name = fields.Char(string='Name', required=True)
    age = fields.Integer(string='Age')
    gender = fields.Selection(string="Gender",selection=[  # selection= is required when we want access key(male,female,other) in xml file
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'other'),
    ], default='other')
    
    description = fields.Text(string='Description')
    state = fields.Selection(string="Status",selection=[ 
        ('draft', 'Draft'),
        ('confirm', 'Confirmed'),
        ('done', 'Done'),
        ('cancel','Cancelled'),
    ], default='draft')

    active= fields.Boolean(string='Active',default=True)
    admit_fee= fields.Float(string='Registration Fee',default=0.0)
    additional_fee= fields.Float(string='Additional Fee',default=100.0)
    total_fee= fields.Integer(string='Total Fee',readonly=True)

    @api.onchange('admit_fee','additional_fee') #this decorator used for live changes in feild values
    def _onchange_total_fee(self):
        if self.admit_fee<0:
             raise UserError('Registration Fee must be greater than 0')

        self.total_fee=self.admit_fee+self.additional_fee


    @api.constrains('additional_fee')   
    def _check_additional_fee(self):  #its will check for all records
            for record in self:
                if record.additional_fee<100.0:
                    raise ValidationError("Additional Fee should be greater than 100.0 your enter Additional Fee is : ",record.additional_fee)

    def action_confirm(self):
        self.state = 'confirm'

    def action_done(self):
        self.state = 'done'
    
    def action_draft(self):
        self.state = 'draft'
    
    def action_cancel(self):
        self.state = 'cancel'
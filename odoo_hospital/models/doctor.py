# -*- coding: utf-8 -*-
from odoo import api, fields, models, _


class HospitalDoctor(models.Model):
    _name = "hospital.doctor"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Hospital Doctor"
    _rec_name = 'doctor_name'
    _order = 'id desc'

    doctor_name = fields.Char(string='Name', required=True, tracking=True)
    age = fields.Integer(string='Age',copy=False)
    gender = fields.Selection(string="Gender",selection=[  # selection= is required when we want access key(male,female,other) in xml file
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'other'),
    ], default='other')    
    note = fields.Text(string='Description')
    # image = fields.Binary(string="Patient Image")
    # appointment_count = fields.Integer(string='Appointment Count', compute='_compute_appointment_count')
    active = fields.Boolean(string="Active", default=True)
    image_d1= fields.Binary(string="Docotr Image")


    # def _compute_appointment_count(self):
    #     for rec in self:
    #         appointment_count = self.env['hospital.appointment'].search_count([('doctor_id', '=', rec.id)])
    #         rec.appointment_count = appointment_count

    

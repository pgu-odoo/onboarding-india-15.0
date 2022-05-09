# -*- coding: utf-8 -*-
# from atexit import register
from multiprocessing import context
from odoo import api, fields, models,_
from odoo.exceptions import UserError, ValidationError


class HospitalAppointment(models.Model):
    _name = "hospital.appointment"     #this model is showing in technical>model after installing(or upgrading) module
    _description = "Hospital Appointment"
    _inherit = ['mail.thread','mail.activity.mixin']    #inherit mail models for chatter to form view in patient

    name = fields.Char(string='Name',related='patient_id.name') #if u set required=True here then u have to must include this field into form and u have to fill it
    patient_id = fields.Many2one('hospital.patients',string='patient')
    age = fields.Integer(string='Age',related='patient_id.age') #related used for to automatically get the age of that patient
    # gender = fields.Selection(string="Gender",related='patient_id.gender') 
    gender = fields.Selection(string="Gender",selection=[  # selection= is required when we want access key(male,female,other) in xml file
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'other'),
    ], default='other')
    description = fields.Text(string='Description',related='patient_id.description')
    state = fields.Selection(string="Status",selection=[ 
        ('draft', 'Draft'),
        ('confirm', 'Confirmed'),
        ('done', 'Done'),
        ('cancel','Cancelled'),
    ], default='draft', tracking=True)
    date_appointment= fields.Date(string='Date')  
    date_appointment_time= fields.Datetime(string='Checkup Time')
    date_closed= fields.Datetime(string='Date end')
    date_start= fields.Datetime(string='Date Start')
    active= fields.Boolean(string='Active',default=True)    
    family_member_id=fields.Many2one(string='Family Member',comodel_name='res.partner',related='patient_id.family_member_id')       #('res.partner', string='Family Member') if we write key value as first argument then we doesn't need to specify its key name- comodel_name'    
    reference= fields.Char(string='Number', readonly=True, default='New')  # for a sequece number
    prescription_line_ids= fields.One2many('appointment.prescription.lines','appointment_id',string='Prescription Line')
    patients_group= fields.Many2many('hospital.patients', string='Patient Group')
    image_101=fields.Binary(string='Patient Image')

    def action_confirm(self):       ##its used for Confirm button given in form view inside header ,control status bar
        self.state = 'confirm'

    def action_done(self):          #used for Done button
        self.state = 'done'
    
    def action_draft(self):
        self.state = 'draft'
    
    def action_cancel(self):
        self.state = 'cancel'

    @api.model                  #used for override existing model
    def create(self,vals):      #override create method,useful during creat record, vals arg contains the record present in the form view (vals are in dict format) #invoke on create to save button 
        # if not vals['description']:
        #     vals['description']="New Patients"
        if vals.get('reference','New')=='New':      #it change the sequence number 'New' to latest one taken from ir.sequence model
            vals['reference']=self.env['ir.sequence'].next_by_code('appointment.sequence')  #its work after click on save button, try to find solution for change auto on click create
        res= super(HospitalAppointment, self).create(vals)  #when we click on create button changes will apply
        return res

    #alternative of  attribute related=patient_id.gender in gender field 
    @api.onchange('patient_id')  #it's invoke _onchange_ fun when any changes appear in patient_id
    def _onchange_patient_id(self):
        if self.patient_id:
            if self.patient_id.gender:    #its looks for Patient_id(Many2one) gender field
                self.gender = self.patient_id.gender
        else:
            self.gender = None  #if patient_id is empty then gender also set to none


class AppointmentPrescriptionLines(models.Model):
    _name = "appointment.prescription.lines"     
    _description = "Appointment Prescription Lines"
    
    name=fields.Char(string='Medicine',required=True)
    qty=fields.Integer(string='Quantity')
    appointment_id=fields.Many2one('hospital.appointment',string='appointment id')
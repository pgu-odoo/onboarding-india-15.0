# -*- coding: utf-8 -*-
# from atexit import register
from tabnanny import check
from yaml import add_implicit_resolver
from odoo import api, fields, models,_
from odoo.exceptions import UserError, ValidationError


class HospitalPatients(models.Model):
    _name = "hospital.patients"     #its create patients table with below Columns name
    _description = "hospital patients"
    _inherit = ['mail.thread','mail.activity.mixin']    #inherit mail models for chatter to form view in patient
    # _rec_name = 'age'   #used in Many2many field for selecting data based on particulat field name(age)
    # _sql_constraints=[('check_age','CHECK(age>100)','age should not greater than 100')]
    # _sql_constraints=[('check_additional_fee','CHECK(additional_fee >= 100.0)',"Additional Fee should be greater than 100.0 "),]
    
    age = fields.Integer(string='Age')
    name = fields.Char(string='Name', required=True)
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
    ], default='draft', tracking=True)
    active= fields.Boolean(string='Active',default=True)
    admit_fee= fields.Float(string='Registration Fee',default=0.0)
    additional_fee= fields.Float(string='Additional Fee',default=10.0)
    total_fee= fields.Integer(string='Total Fee',readonly=True)
    family_member_id=fields.Many2one(string='Family Member',comodel_name='res.partner')       #('res.partner', string='Family Member') if we write key value as first argument then we doesn't need to specify its key name- comodel_name'   
    reference= fields.Char(string='Number', default='New', copy=False)   #lambda self: self.env['ir.sequence'].next_by_code('patient.sequence')
    appointment_count= fields.Integer(string='Appointment Count', compute='compute_appointment_count')
    appointment_ids=fields.One2many('hospital.appointment','patient_id',string='Appointment ID')
    image= fields.Binary(string='Patient Image')

    def compute_appointment_count(self):
        for rec in self:        #without for loops if we used appointment_count in list view then its gives as singleton error
            rec.appointment_count=self.env['hospital.appointment'].search_count([('patient_id','=',rec.id)])
        
    @api.onchange('admit_fee','additional_fee') #this decorator used for live changes in feild values,whenever change occurs in passing parameter field then _onchange_ function call automatically, first time fun auto call when click the create button.. after auto call when we change the field 
    def _onchange_total_fee(self):
        if self.admit_fee<0:
            raise UserError('Registration Fee must be greater than 0')
        self.total_fee=self.admit_fee+self.additional_fee

    # @api.constrains('additional_fee') 
    # def _check_additional_fee(self):  #its will check for all records
    #         for record in self:
    #             if record.additional_fee<100.0:
    #                 raise ValidationError(_("Additional Fee should be greater than 100.0 your enter Additional Fee is : %s" %record.additional_fee))

    def action_confirm(self):       ##its used for Confirm button given in form view inside header ,control status bar
        self.state = 'confirm'

    def action_done(self):          #used for Done button
        self.state = 'done'
    
    def action_draft(self):
        self.state = 'draft'
    
    def action_cancel(self):
        self.state = 'cancel'

    @api.model                  #used for override existing model
    def create(self,vals):      #override create method,useful during creat record, vals arg contains the record present in the form view (vals are in dict format) #invoke on click save button 
        res= super(HospitalPatients, self).create(vals)
        if vals.get('reference','New')=='New':
            vals['reference']=self.env['ir.sequence'].next_by_code('patient.sequence')   #res.reference=self.,,
        if not vals['description']:
            vals['description']="New Patients"
        
        #     if vals.get('reference','New')=='New':      #it change the sequence number 'New' to latest one taken from ir.sequence model
        #         vals['reference']=self.env['ir.sequence'].next_by_code('patient.sequence')  #its work after click on save button, try to find solution for change auto on click create
          #when we click on save button aboce changes will apply and write this part end otherwise changes will not catch
        return res

    # def write(self,vals):       #override write method,doen't need decorator ,useful for edit  existing record
        
    #     if vals.get('name','ketan')=='ketan':    #vals['name']=='ketan' its not working
    #         vals['name']="kkt"
        
    #     res= super(HospitalPatients, self).write(vals)
    #     return res

    def unlink(self):      #usefull when we delete record(by action menu) ::its override unlink method

        if self.state == 'done':
            raise ValidationError(_("You can't delete %s as it is in DONE state" % self.name))
        res= super(HospitalPatients,self).unlink()
        
        return res

    # @api.model
    # def default_get(self,fields):  #invole when click on creat button
    #     import pdb
    #     pdb.set_trace()
    #     res= super(HospitalPatients, self).default_get(fields)  #its returns key:value pairs of variable that have default value given
        
    #     res['reference']=self.env['ir.sequence'].next_by_code('patient.sequence')
    #     if not res.get('gender'):
    #         res['gender']='male'
    #     return res

# solution for to get the sequence number correctly without changes two times and without new keyword
    def copy(self,default=None):
        if default is None: 
           default = {}
        if not default.get('name'):
           default['name'] = '%s (copy)' %self.name
        default['description']='Copied Record'
        
        res=super(HospitalPatients,self).copy(default)
        # res.reference=self.env['ir.sequence'].next_by_code('patient.sequence') 
        return res


    @api.constrains('name') 
    def check_name(self):  #its will check for all records
            for record in self:
                patient=self.env['hospital.patients'].search([('name','=', record.name),('id',"!=",record.id)])
                if patient:
                    raise ValidationError(_("Name %s is already in exists" % record.name))

        
    @api.constrains('age') 
    def check_age(self):  #its will check for all records
            for record in self:                
                if record.age==0:
                    raise ValidationError(_("Age can't be ZERO"))

        
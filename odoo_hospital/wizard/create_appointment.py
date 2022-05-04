# -*- coding: utf-8 -*-
from odoo import api, fields, models,_
from odoo.exceptions import UserError, ValidationError


class CreateAppointmentWizard(models.TransientModel):
    _name = "create.appointment.wizard"     
    _description = "create appointment wizard"
    
    name = fields.Char(string='Name')
    appointment_date= fields.Datetime(string='Appointment date')
    patient_id = fields.Many2one('hospital.patients',string='patient',required=True)

    def action_create_appointment(self):   #it will invoke when we click on create button of wizard
        #task: onclick create button my data will be created on appointment form 
        vals={
            'patient_id':self.patient_id.id,
            'date_appointment':self.appointment_date,
            }
        appointment_rec=self.env['hospital.appointment'].create(vals)   # here new appointment is created with above vals dict ,it's store into hospital.appointment(/id/,)
        return {
            'name': 'Appointment',
            'type': 'ir.actions.act_window',
            'view_mode': 'form',
            'res_model': 'hospital.appointment',
            'res_id': appointment_rec.id,     
              }
    
    def action_view_appointment(self):
        action = self.env.ref('odoo_hospital.action_hospital_appointment').read()[0]  #or action = self.env['ir.actions.actions']._for_xml_id("odoo_hospital.action_hospital_appointment")
        action['domain'] = [('patient_id', '=', self.patient_id.id)]
        return action
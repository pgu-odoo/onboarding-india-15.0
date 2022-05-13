# -*-encoding: utf:8 -*-

from odoo import models,fields

class PatientWizard(models.TransientModel):
    _name = 'patient.wizard'
    _description = 'Patient wizard to see the patient name with their bills'


    # def _default_patient(self):
    #     return self.env['hospital.patient'].browse(self._context_get('active_id'))


    patient_name_bill = fields.Many2one(comodel_name='hospital.patient',
                                        string='Patient Name')
    gender = fields.Selection([('male','Male'),('female','Female'),('other','Other')])
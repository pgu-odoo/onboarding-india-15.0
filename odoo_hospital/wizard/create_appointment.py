# -*- coding: utf-8 -*-

from odoo import api, fields, models,_
from odoo.exceptions import UserError, ValidationError

class CreateAppointmentWizard(models.TransientModel):
    _name = "create.appointment.wizard"     
    _description = "create appointment wizard"
    

    name = fields.Char(string='Name', required=True)

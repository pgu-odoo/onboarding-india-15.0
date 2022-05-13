from odoo import api, fields, models, _

class HospitalAppointment(models.Model):

    #CLASS ATTRIBUTES
    _name = "hospital.appointment"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Hospital Appointment"
    _order = "doctor_ids,name,age"

    #BASIC FIELDS
    name = fields.Char(string='Order Reference', required=True, copy=False, readonly=True,
                       default=lambda self: _('New'))
    patient_ids = fields.Many2one('hospital.patient', string="Patient")
    age = fields.Integer(string='Age', related='patient_ids.age', tracking=True, store=True)
    doctor_ids = fields.Many2one('hospital.doctor', string="Doctor")
    state = fields.Selection([('create', 'Appointment Created'),('confirm','confirmed'),
                              ('done', 'Done'), ('cancel', 'Cancelled')],
                             string="State", tracking=True)
    note = fields.Text(string='Description')
    date_appointment = fields.Date(string="Date")
    date_checkup = fields.Datetime(string="Check Up Time")
    prescription = fields.Text(string="Prescription")
    prescription_line_ids = fields.One2many('appointment.prescription.lines', 'appointment_ids',
                                            string="Prescription Lines")

    #BUTTON METHODS
    def action_create(self):
        self.state = 'create'

    def action_confirm(self):
        self.state = 'confirm'

    def action_cancel(self):
        self.state = 'cancel'

    def action_done(self):
        self.state='done'

    #SEQUENCE METHOD
    @api.model
    def create(self,vals):
         if vals.get('name', _('New')) == _('New'):
             vals['name'] = self.env['ir.sequence'].next_by_code('hospital.appointment') or _('New')
         res = super(HospitalAppointment, self).create(vals)
         return res


class AppointmentPrescriptionLines(models.Model):
            _name = "appointment.prescription.lines"
            _description = "Appointment Prescription Lines"

            name = fields.Char(string="Medicine", required=True)
            qty = fields.Integer(string="Quantity")
            appointment_ids = fields.Many2one(comodel_name='hospital.appointment', string="Appointment")
from odoo import api, fields, models, _



class HospitalAppointment(models.Model):

    #CLASS ATTRIBUTES
    _name = "hospital.appointment"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Hospital Appointment"
    _order = "doctor_id,name,age"

    name = fields.Char(string='Order Reference', required=True, copy=False, readonly=True,
                       default=lambda self: _('New'))
    reference = fields.Char(string="Order.reference", copy=False,
                            readonly=True)
    patient_id = fields.Many2one('hospital.patient', string="Patient", required=True)
    age = fields.Integer(string='Age', related='patient_id.age', tracking=True, store=True)
    doctor_id = fields.Many2one('hospital.doctor', string="Doctor", required=True)
    state = fields.Selection([('create', 'Appointment Created'),('confirm','confirmed'),
                              ('done', 'Done'), ('cancel', 'Cancelled')],
                             string="State", tracking=True)
    note = fields.Text(string='Description')
    date_appointment = fields.Date(string="Date")
    date_checkup = fields.Datetime(string="Check Up Time")
    prescription = fields.Text(string="Prescription")
    prescription_line_ids = fields.One2many('appointment.prescription.lines', 'appointment_id',
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


class AppointmentPrescriptionLines(models.Model):
            _name = "appointment.prescription.lines"
            _description = "Appointment Prescription Lines"

            name = fields.Char(string="Medicine", required=True)
            qty = fields.Integer(string="Quantity")
            appointment_id = fields.Many2one('hospital.appointment', string="Appointment")
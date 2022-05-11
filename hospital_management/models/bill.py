from odoo import fields,models,api,_

class HospitalBill(models.Model):
    _name = "hospital.bill"
    _description  = "Patient Bill"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _rec_name = "bill_id"

    no = fields.Integer(string='Bill_No..', required=True)
    image = fields.Binary(string='Patient_Image')
    bill_id = fields.Many2one(comodel_name="hospital.patient",string="Bill",tracking=True)
    p_name = fields.Many2one(comodel_name="hospital.patient",string='Patient_name',tracking=True)
    doctor_charges = fields.Float(string="Doctor Charge",tracking=True)
    medicine_charges = fields.Float(string="Medicine Charge",tracking=True)
    room_charge = fields.Float(string="Room Charges",tracking=True)
    operation_charge = fields.Float(string="Operation Charges",tracking=True)
    nursing_charge = fields.Float(string="Nursing Charges",tracking=True)
    total = fields.Float(string="Total",compute="_total")
    note = fields.Html(string="Note")


    @api.depends('doctor_charges','medicine_charges','room_charge','operation_charge','nursing_charge')
    def _total(self):
        """
        THIS METHOD WILL COUNT THE TOTAL CHARGE
        :return:
        """
        for hospital in self:
            hospital.total = hospital.doctor_charges + hospital.medicine_charges + \
                             hospital.room_charge + \
                             hospital.operation_charge + \
                            hospital.nursing_charge

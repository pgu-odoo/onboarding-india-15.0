from odoo import fields,models,api,_
from odoo.exceptions import UserError, ValidationError

class HospitalBill(models.Model):
    _name = "hospital.bill"
    _description  = "Patient Bill"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _rec_name = "p_name"

    no = fields.Integer(string='Bill_No..', required=True)
    image = fields.Binary(string='Patient_Image')
    bill_ids = fields.Many2one(comodel_name="hospital.patient",string="Bill",tracking=True,ondelete='cascade')
    p_name = fields.Many2one(comodel_name="hospital.patient",string='Patient_name',tracking=True)
    doctor_charges = fields.Float(string="Doctor Charge",tracking=True)
    medicine_charges = fields.Float(string="Medicine Charge",tracking=True)
    room_charge = fields.Float(string="Room Charges",tracking=True)
    operation_charge = fields.Float(string="Operation Charges",tracking=True)
    nursing_charge = fields.Float(string="Nursing Charges",tracking=True)
    total = fields.Float(string="Total", readonly=True,group_operator='avg') #,compute="_total"
    note = fields.Html(string="Note")


    # @api.depends('doctor_charges','medicine_charges','room_charge','operation_charge','nursing_charge')
    # def _total(self):
    #     """
    #     THIS METHOD WILL COUNT THE TOTAL CHARGE
    #     :return:
    #     """
    #     for hospital in self:
    #         hospital.total = hospital.doctor_charges + hospital.medicine_charges + \
    #                          hospital.room_charge + \
    #                          hospital.operation_charge + \
    #                         hospital.nursing_charge

    @api.onchange('doctor_charges','medicine_charges','room_charge','operation_charge','nursing_charge')
    def _onchange_total_cost(self):
        if self.medicine_charges or self.nursing_charge or self.doctor_charges < 0.0:
            import pdb
            pdb.set_trace()
            raise UserError('Charges Cannot be negative!!!')
        self.total = self.doctor_charges + self.medicine_charges+ self.room_charge + self.medicine_charges + self.nursing_charge


    # @api.constrains('doctor_charges','medicine_charges')
    # def check_charges(self):
    #     if self.medicine_charges or self.doctor_charges < 1:
    #         raise ValidationError("Values Or Charges Cannot be less then 1")

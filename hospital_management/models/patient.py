from odoo import api,fields, models,_

class HospitalPatient(models.Model):
        #CLASS ATTRIBUTE
        _name = "hospital.patient"
        _inherit = ["mail.thread",'mail.activity.mixin']
        _description = "Hospital Patient Model"
        _auto = True
        _order = 'name'

        #BASIC FIELDS
        name = fields.Char(string='Name',tracking=True,required=True,placeholder="Enter Your Name",size=3)
        age = fields.Integer(string='Age',tracking=True,required=True)
        weight = fields.Integer(string='Weight',tracking=True)
        disease = fields.Char(string="Disease",required=False)
        status = fields.Boolean(string='Death ?', help='Patient is alive or Death')
        gender = fields.Selection([('male', 'Male'),
                    ('female', 'Female'),
                    ('other', 'Other')],required=False,tracking=True,default='male')
        state = fields.Selection([('draft', 'Draft'),
                                   ('confirm', 'Confirmed'),
                                   ('done', 'Done'),
                                  ('dead','Dead')], default='draft',tracking=True)
        file_name = fields.Char('File_Name')
        document = fields.Binary('Document')
        image = fields.Binary(string="Patient Image")
        address = fields.Char(string="Address",required=True)
        contact_no = fields.Char(string="Contact No.")
        password = fields.Char(string='Password')
        email_id = fields.Char(string='Email_ID')
        al_contact_no = fields.Char(string="Alternative Contact No.")
        date_of_admit = fields.Date(string="Date of Admit",index=True)
        date_of_discharge = fields.Datetime(string="Date of Discharge")
        note = fields.Text(string='Description')
        color = fields.Integer(string="Color_Box")

        #RELATIONAL FIELDS
        partner_ids = fields.Many2one('res.partner', string='Parent_Name')
        doctor_ids = fields.Many2many("hospital.doctor","patient_doctor_rel","patient_id","doctor_id",string='Doctor Name')
        bill_ids = fields.One2many("hospital.bill","p_name",string='Bill Amount',ondelete="restrict")


        #BUTTON METHODS
        def action_confirm(self):
                self.state="confirm"

        def action_draft(self):
                self.state="draft"

        def action_done(self):
                self.state = "done"

        def action_dead(self):
                        self.state = "dead"


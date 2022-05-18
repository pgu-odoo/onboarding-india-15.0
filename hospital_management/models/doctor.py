from odoo import  fields, models,_,api

class HospitalDoctor(models.Model):

    #CLASS ATTRIBUTES
    _name = "hospital.doctor"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Hospital Doctor"

    #BASIC FIELDS
    name = fields.Char(string='Name', required=True, tracking=True)
    dob=fields.Date(string="Date of Birth")
    age = fields.Integer(string='Age', tracking=True, copy=False)
    doj = fields.Datetime(string='Date Of Joining')
    available = fields.Boolean(string="Available", default=True)
    salary = fields.Float(string="Salary",digits=(5,6))
    rating = fields.Selection([(str(ele),str(ele)) for ele in range(6)],'Ratings')
    color = fields.Integer(string="Color")
    department = fields.Selection([('param','Paramedical Department'),
                                   ('surge','Surgical Department'),
                                   ('pharm','Pharmacy Department'),('radio','Radiology Department'),
                                   ('radio','Radiology Department'),('cardio','Cardiology Department')])
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    ], required=True, default='male', tracking=True)
    url = fields.Char(string='Website')
    note = fields.Text(string='Description')
    image = fields.Binary(string="Patient Image")
    appointment_count = fields.Integer(string='Appointment Count', compute='_compute_appointment_count')
    doctor_code = fields.Char(string='Unique Code')
    @api.model
    def _cron_hospital_doctor_availability(self):
        print("Doctor is Available")

    #COMPUTE METHOD
    def _compute_appointment_count(self):
        """
        THIS METHOD WILL COUNT APPOINTMENT
        :return:
        """
        for rec in self:
            appointment_count = self.env['hospital.appointment'].\
                        search_count([('doctor_ids', '=', rec.id)])
            rec.appointment_count = appointment_count

    #OVERRIDE CREATE METHOD
    @api.model_create_multi
    def create(self,vals_list):
        """
        Overridden create() method to set the code from the name
        :param vals_list:
        :return:
        """
        for vals in vals_list:
            if not vals.get('doctor_code',False):
                vals['doctor_code'] = vals.get('name')[:4].upper() + '(copy)'
                res = super().create(vals_list)
                print("Create Override",res)
                return res
from odoo import  fields, models,_,api
from odoo.exceptions import ValidationError

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

    #OVERRIDE UNLINK METHOD
    def unlink(self):
        """
        This method overridden the unlink() method
        :return:
        """
        if self.available == True:
            raise ValidationError("Doctor is Available You Cannot delete The record")
        return super().unlink()

    #OVERRIDE WRITE METHOD
    def write(self,vals):
        """
        This Method overridden write() method
        :param vals:
        :return:
        """
        if vals.get('name',False):
            vals['doctor_code'] = vals.get('name')[:3].upper() + vals.get('gender')[2].lower()
            res = super().write(vals)
            print("Successfully Override Write Method",res)
            return res

    #OVERRIDE COPY METHOD
    def copy(self,default=None):
        """
        This method overridden Duplicate() or Copy() method
        :param default:
        :return:
        """
        default = {
            'name' : self.name + '(copied)'
        }
        res = super().copy(default=default)
        print("Successfully Override Copy Method",res)
        return res
    #
    # @api.constrains('note')
    # def check_note_length(self):
    #     """
    #     This method checks the length of client_id
    #     :return:
    #     """
    #     if len(self.note) > 5:
    #         raise ValidationError("Entered Value should not be more than 5")
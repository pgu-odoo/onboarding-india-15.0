from odoo import api,fields, models,_,exceptions
from odoo.exceptions import ValidationError

class HospitalPatient(models.Model):
        #CLASS ATTRIBUTES

        #TECHNICAL_NAME
        _name = "hospital.patient"
        _inherit = ["mail.thread",'mail.activity.mixin']
        #FUNCTIONAL_NAME
        _description = "Hospital Patient Model"
        # _table = 'patient_patient'
        _auto = True
        _order = 'name'

        #FOR ADDING SQL CONSTRAINTS THROUGH CLASS ATTRIBUTE
        _sql_constraints = [
                ('unique_contact_no', 'unique(contact_no)','The Contact No. must be Unique!'),
                ('check_weight', 'check(weight<100)', 'The Patient weight should not be more than 100!'),
                ('check_description','not null(note)','The Description should not be null')

        ]

        #BASIC FIELDS
        reference = fields.Char(string='Order Reference',readonly=True,copy=False,required=True,default=lambda self: _('New Patient'))
        name = fields.Char(string='Name',tracking=True,required=True,placeholder="Enter Your Name",size=20)
        age = fields.Integer(string='Age',tracking=True,required=True)
        dob =  fields.Date(string='Date Of Birth')
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
        note = fields.Html(string='Description')
        color = fields.Integer(string="Color_Box")
        currency_id = fields.Many2one(comodel_name='res.currency', string='Currency')

        #RELATIONAL FIELDS
        partner_ids = fields.Many2one('res.partner', string='Parent_Name')
        doctor_ids = fields.Many2many("hospital.doctor","patient_doctor_rel","patient_id","doctor_id",string='Doctor Name')
        bill_ids = fields.One2many("hospital.bill","p_name",string='Bill Amount',ondelete="restrict")

        #CONSTRAINTS FOR MATCHING AGE AND DATE OF BIRTH
        @api.constrains('dob','age')
        def check_age_dob(self):
                """
                Compare patient's Age and Date of Birth
                :return:
                """
                cr_dt = fields.Date.today()
                for patient in self:
                        if patient.age and patient.dob:
                                ag = cr_dt.year - patient.dob.year
                                if ag != patient.age:
                                        raise ValidationError("Age and Date of Birth are not matching")

        #BUTTON METHODS
        def action_confirm(self):
                self.state="confirm"

        def action_draft(self):
                self.state="draft"

        def action_done(self):
                self.state = "done"

        def action_dead(self):
                        self.state = "dead"

        #METHOD FOR GETTING PATIENTS BILLS
        def get_patient_bill(self):
                """
                This method will get the bills of the Patients
                :return:
                """
                bill_obj = self.env['hospital.bill']
                for patient in self:
                        bills = patient.bill_ids
                action = self.env.ref('hospital_management.action_Bill').read()[0]
                print('ACTION',action)
                action['domain'] = [('id','in',bills.ids)]

        #METHOD FOR SEQUENCE
        @api.model
        def create(self, vals):
                if vals.get('reference', _('New')) == _('New'):
                        vals['reference'] = self.env['ir.sequence'].next_by_code('hospital.patient') or _('New')
                res = super(HospitalPatient, self).create(vals)
                return res

        #BUTTON METHOD FOR PERFORMING SOME TEST
        def test(self):
                """
                This is a button method which will be called on a button
                click and will perform some test
                :return:
                """
                print("Hello!!!!")
                patients = self.search([])
                print("Patients",patients)

                #RECORDSET METHODS

                #Filtering based on some specific value in the field.
                male_patients = patients.filtered(lambda r:r.gender == 'male')
                print('Male Patients',male_patients)
                female_patients = patients.filtered(lambda r:r.gender == 'female')
                print('Female Patients',female_patients)

                #Mapping of records to form a list
                patient_names = patients.mapped('name')
                print('Patient Names',patient_names)
                patient_gender = patients.mapped('gender')
                print('Patient Gender',patient_gender)
                #Mapping with multiple fields
                patient_list = patients.mapped(lambda r:r.name +'__' + str(r.id))
                print('Patient_with_multiple_field',patient_list)

                #Sorting records based on a field
                arranged_patients = patients.sorted('name')
                print('Arranged Patient',arranged_patients)
                #With Keyword parameter and reverse order
                arranged_patients = patients.sorted(key='name',reverse=True)
                print("Arranged Patients with Keyword",arranged_patients)
                #Using lambda
                arranged_patients = patients.sorted(key=lambda r:r.id)
                print("Arranged Parents",arranged_patients)

                #SET OPERATIONS
                for mp in male_patients:
                        if mp in patients:
                                print("Child")

                        if mp not in female_patients:
                                print("Not a Child")

                #SUBSET
                #Male patients set is a subset of patients set
                if male_patients < patients:
                        print("Male Patient is a Subset of a Patient")
                #Male patients set is not a subset of female patients set
                if male_patients < female_patients:
                        print("Male Patient is not a Subset of Female Patients")
                #The male patients can not be its own subset
                if male_patients < male_patients:
                        print("Male Patients Can not be Own Subset")

                #SUPERSET
                #Patients is a superset of female_patients
                if patients > female_patients:
                        print("Patients is a superset of female patients")
                #Patients is not a superset of itself
                if patients > patients:
                        print("Patients not be superset of itself ")
                #If we use the >= sign then it can be its own superset
                if patients >= patients:
                        print("Superset")

                #OPERATIONS:
                #UNION OPERATION
                res = male_patients | female_patients
                print('Union Operation',res)

                #INTERSECTION OPERATION
                res = male_patients & female_patients
                print("Intersection Operation",res)

                #DIFFERENCE OPERATION
                res = patients -male_patients
                print("Difference Operation",res)


        #ORM METHODS
        def create_record(self):
                """
                This method is used to demonstrate the ORM method create
                --------------------------------------------------------------------------------
                :return:
                """
                vals_list = []
                vals = {
                        'name':'Nisha Gupta',
                        'age' : 34,
                        'gender':'male',
                        'notes':'<h1>This is a test Template</h1>',
                        'date_of_admit':fields.Datetime.now(),
                        })],
                }
                vals_list.append(vals)
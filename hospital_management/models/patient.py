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
        # _order = 'name'
        _order = 'sequence'

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
        sequence = fields.Integer('Sequence')
        document = fields.Binary('Document')
        image = fields.Binary(string="Patient Image")
        address = fields.Char(string="Address",required=True)
        contact_no = fields.Char(string="Contact No.")
        password = fields.Char(string='Password')
        email_id = fields.Char(string='Email_ID')
        al_contact_no = fields.Char(string="Alternative Contact No.")
        date_of_admit = fields.Datetime(string="Date of Admit",index=True)
        date_of_discharge = fields.Datetime(string="Date of Discharge")
        note = fields.Html(string='Description')
        color = fields.Integer(string="Color_Box")
        currency_id = fields.Many2one(comodel_name='res.currency', string='Currency')
        amount = fields.Monetary(currency_fields=currency_id,string='Amount')
        ref_id = fields.Reference(selection= [
                        ('hospital_patient','name'),
                        ('hospital_appointment','reference')
                                        ])

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
                print("Current Language Of System",self.env.lang)
                print("Company Name",self.env.company)
                print("Current_User",self.env.user)
                print("Context",self.env.context)
                print("recordset",self.env.ref('hospital_management.view_appointment_form'))
                print("Metadata",self.get_metadata())

                #CURRENT_USER
                current_user  = self.env['res.users'].search([('login','=','admin')])
                print("Current User",current_user)

                patients = self.search([])
                doctors = self.env['hospital.doctor'].search([])
                print("Patients",patients)
                print("Doctors",doctors)
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
        #CREATE METHOD
        def create_record(self):
                """
                This method is used to demonstrate the ORM method create
                --------------------------------------------------------------------------------
                :return:
                """
                vals_list = []
                #A dictionary containing fields and their respective values
                vals = {
                        'name':'Vishal Singhaniya',
                        'age' : 34,
                        'gender':'male',
                        'address':'Kanoj',
                        'note':'<h1>This is a test Template</h1>',
                        'date_of_admit':fields.Datetime.now(),
                        'bill_ids':[(0,0, {
                                'no':4655,
                                'p_name':self.id,
                                'doctor_charges':345.98,
                                'medicine_charges':465.98,
                        })],
                        'doctor_ids':[(6,0,[4,6])]
                }
                vals_list.append(vals)
                patient = self.create(vals_list)
                print("New Patient",patient)

                #CREATING RECORD IN ANOTHER MODEL

                doc_obj = self.env['hospital.doctor']
                vals_list = [
                        {
                        'name':'Kunal Chabra',
                        'age' : 34,
                        'gender':'male',
                        'department':'pharm',
                        'doj':fields.Datetime.today()
                        }
                ]
                doctor = doc_obj.create(vals_list)
                print("New Doctor",doctor)


        #WRITE METHOD
        def update_record(self):
                """
                This method demonstrates the usage of write() and browse() method
                ------------------------------------------------------------------------------------------
                :return:
                """

                vals = {
                        'note':'<h3>The Record is Updated</h3>',
                        'gender':'male',
                }
                res = self.write(vals)
                print(res)

        #UPDATE RECORD USING BROWSE METHOD
                doc_obj = self.env['hospital.doctor']
                doctor = doc_obj.browse(2)
        #UPDATING RECORD OF ANOTHER MODEL
                res = doctor.write({
                'age':45,
                'gender':'female'
                })
                print(res)

        #COPY METHOD
        def copy_record(self):
                """
                This method demonstrates the copy method
                ----------------------------------------------------------
                :return:
                """
                default = {
                    'dob' : fields.Date.today()
                }
                new_rec = self.copy(default=default)
                print("Copy Done",new_rec)

        #READ METHOD
        def read_record(self):
                """
                This method demonstrates read method
                :return:
                """
                patient_dict = self.read()
                print("Read Patient",patient_dict)

                patient_dict = self.read(
                        fields=['name',
                                'age',
                                'gender',
                                'bill_ids',
                                'doctor_ids'
                                ],load='')
                print("Reading Patient's Details Based on some specific Field",patient_dict)

                #READING ANOTHER MODEL FIELD'S DATA
                doctor_obj  =self.env['hospital.doctor'].browse(1)
                doctor = doctor_obj.read(
                        fields=[
                                'name',
                                'age',
                                'doj',
                                'salary'
                        ]
                )
                print('Read Doctor',doctor)

        #UNLINK METHOD
        def delete_record(self):
                """
                This method demonstrates the unlink() method
                ---------------------------------------------------------------
                :return:
                """
                self.unlink()

                #DELETING ANOTHER MODEL'S RECORD
                doc_obj = self.env['hospital.doctor'].browse()
                doctor = doc_obj.unlink()
                print("Record is deleted",doctor)

        #SEARCH METHOD
        def search_record(self):
                """
                This method demonstrates the search() and search_count() method
                ----------------------------------------------------------------------------------------
                :return:
                """

                #EMPTY DOMAIN WILL GIVE ALL THE RECORDS
                patients =self.search([])
                print("All Patients List",patients)

                #FOR DIFFERENT MODEL
                #DOMAIN WILL RETURN SPECIFIC RECORD
                doctor_obj = self.env['hospital.doctor'].search([('gender','=','male')])
                print('Male Doctor', doctor_obj)

                #OFFSET USED TO SKIP NO OF RECORDS
                patients_skipped = self.search([],offset=2)
                print('Patients Skipped',patients_skipped)

                #LIMIT USE DTO VIEW SPECIFIC NO OF RECORDS
                patients_limited = self.search([],limit=2)
                print("Limited Patients",patients_limited)

                #USING LIMIT AND OFFSET TOGETHER
                patients_skip_limited = self.search([],offset=1,limit=3)
                print('Patients Skip and Limited',patients_skip_limited)

                #OREDR USED TO VIEW SORT THE RECORDS
                patients_mixed = self.serach([],offset=1,limit=4,order='age')
                print("Mixed Patients",patients_mixed)

                #COUNT TO GET THE NO OF RECORDS USING SEARCH METHOD
                no_of_male_patients = self.search([('gender','=','male')],count=True)
                print("Male Patients",no_of_male_patients)

                #COUNT TO GET THE NO OF RECORDS USING SEARCH_COUNT METHOD
                no_of_female_patients = self.search_count([('gender', '=', 'male')])
                print("Male Patients", no_of_female_patients)

        #SEARCH READ METHOD
        def search_read_record(self):
                """
                This method demonstrates the search_read() method
                ----------------------------------------------------------------------
                :return:
                """
                res = self.search_read()
                print(res)

                #SEARCH_READ WITH SPECIFIC DOMAIN
                res = self.search_read(domain=[('gender','=','female')])
                print("Female Patients",res)

                #SEARCH_READ WITH SPECIFIC DOMAIN AND FIELDS AND CONDITION
                res = self.search_read(domain=[('gender','=','male')],
                                       fields=['name','age','dob'],
                                       offset=1,
                                       limit=3,
                                       order='name')
                print('Male Patients with Some Specific Condition and fields',res)


        #READ_GROUP METHOD
        def read_group_record(self):
                """
                This Method demonstrates the read-group method
                -------------------------------------------------------------------
                :return:
                """
                patients = self.read_group(domain=[],
                                           fields=['age','state','status'],
                                           groupby=['gender','state'],
                                           lazy=True)
                print("Patients By Read_group Method",patients)

                #Note:-Lazy=True means it is also count gender also

                patients = self.read_group(domain=[],
                                           fields=['age', 'state', 'status'],
                                           groupby=['gender', 'state'],
                                           lazy=False)
                print("Patients By Read_group Method", patients)
        @api.model
        def name_searc(self,name='',args=None,operator='ilke',limit=10):
                """
                Overridden name_search method to search based on name and type
                -----------------------------------------------------------------------------------------
                :param name:
                :param args:
                :param operator:
                :param limit:
                :return:
                """

                domain = ['|',('gender',operator,name)]
                if args:
                        domain += args
                patient = self.search(domain, limit=limit)
                return patient.name_get()
        # @api.model
        # def default_get(self, fields_list):
        #         """
        #         Overridden default_get method to update the default values
        #         :param self:
        #         :param fields_list: List of all fields passed to get the default value
        #         :return: A dictionary containing fields and their default values
        #         """
        #         print("Fields",fields_list)
        #         doc_obj = self.env['hospital.doctor']
        #         doctor= doc_obj.super().default_get(fields_list)
        #         if 'age' in doctor:
        #                 doctor['url'] = 'https://www.odoo.com'
        #                 print(doctor)
        #         return doctor

        @api.onchange('gender')
        def onchange_gender(self):
                """
                Onchange method to set fees based on gender
                :return:
                """
                res = {}
                for patient in self:
                        if patient.gender == 'male':
                                patient.age = 67
                        elif patient.gender == 'female':
                                patient.age = 45
                        else:
                                res = {
                                        'warning': {
                                                'title' : 'Warning!',
                                                'message' : 'You should select a gender!'
                                        }
                                }
                        patient.age = 0.0
                return res
from odoo import models,fields,api,_
from odoo.exceptions import UserError,ValidationError
from datetime import timedelta



class HospitalAppointment(models.Model):

	_name = 'hospital.appointment'
	_description = 'Patient Appointment' 


	Appointmentid = fields.Integer(string="Appointment Id")

	treatment_price=fields.Float(string="Base Price",default=500.00)
	additional_price=fields.Float(string="Additional_fee",default=20.00)
	total_price=fields.Float(string="Total_Price",compute="_compute_total_fees")

	datetime = fields.Datetime(string="date time")
	description=fields.Text(string='Description')

	state=fields.Selection([('draft','Draft'),('confirm','Confirm'),('done','Done'),('cancel','Cancelled')],default='draft',string="Status")

	#doctor_ids=fields.Many2many(string='Doctor',)



	def action_confirm(self):
		self.state='confirm'

	def action_done(self):
		self.state='done'

	def action_draft(self):
		self.state='draft'

	def action_cancel(self):
		self.state='cancel'



	@api.depends('treatment_price','additional_price')

	def _compute_total_fees(self):  #self=hospital.appointment(3,)
		print('--->>',self)
		if self.additional_price<20:
			raise UserError("additional_price is starting with 20 rs")


		self.total_price=self.additional_price+self.treatment_price


	# @api.constrains('Appointmentid')

	# def check_Appointmentid(self):  #trigger this function base on Appointmentid fields 

	# 	for rec in self: # interat "self" inorder to avoid single error 


	# 		appo_id=self.env['hospital.appointment'].search([('Appointmentid','=',rec.Appointmentid)]) #chekc in this 'hospital.appointment ' model that hospital.appointment is alread exist or not 

	# 		if appo_id:
	# 			raise UserError("Appointment id  is already exists")

	# @api.constrains('treatment_price')

	# def check_treatment_price(self):  
	# 	for rec1 in self:
			
	# 		if rec1.treatment_price>1000:
	# 			raise UserError("treatment price is",rec1.treatment_price,"its should be less than 1000")



	@api.onchange('treatment_price') # invoke when we  change in  "additional_fee" 
	def _check_treatment_price(self):
		for record in self:
			print('self ------------------>',record) #record="hospital.appointment(<NewId origin=3>,)"
			if record.treatment_price<10.00:
				raise ValidationError('additional_fee cannot be less than 10: %s'%record.treatment_price)



	@api.ondelete(at_uninstall=False)
	def _check_appointments(self):
		for rec2 in self:
			print('------->>',rec2)
			if rec2.datetime:  #you can't delete this appointment if datetime is assing
				raise UserError("You can't delete this Appointment")


	@api.model
	def create(self,vals):
		print('vals--- is ',vals)
		print('self--- is ',self)
		return super(HospitalAppointment,self).create(vals)


	def write(self,vals):
		print('vals--- is ',vals)
		print('self--- is ',self)
		return super(HospitalAppointment,self).write(vals)





	


	
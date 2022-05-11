# -*- coding: utf-8 -*-
from odoo import models,fields,api,_
from odoo.exceptions import UserError,ValidationError
from datetime import timedelta 




class Course(models.Model):

	_name='academy.course'
	_description='Course info'
	_rec_name = "name"

	# _inherits = {'subject.details': 'related_subject'}  # we inherit all fiels and  methods which is define in "subject.details" to "subject.details"

	# related_subject=fields.Char(string="related_subject")


	# Fields of odoo are  Monetory is use for calculation,Integer ,Float,Boolean,Selection,Text,Char,Html,Date,Datetime
	name =fields.Char(string='Title',required=True) #required True bacause we always have a title
	description=fields.Text(string='Description')
	level=fields.Selection(string='Level',selection=[('beginner','Beginner'),('intermediate','Intermediate'),('advanced','Advanced')],copy=False,default='beginner')
	active =fields.Boolean(string='Active',default=True)

	lecture_date=fields.Date(string="Lecture Date")
	lecture_starttime=fields.Date(string="Lecture_start time")  # default=field.Date.today for by default current date  (lecture_startday)
	lecture_endtime=fields.Date(string="Lecture end time",compute="_compute_lecture_endtime",inverse="_inverse_lecture_endtime",store=True)# inverse fuction use for if someone give enddate instead of duration and store=True for save in DB 


	duration=fields.Integer(string="Lecture duration")

 
	base_price=fields.Float(string="Base Price",default=0.00)
	additional_fee=fields.Float(string="Additional_fee",default=10.00)
	total_price=fields.Float(string="Total_Price",compute='_compute_total_price')

	subjects = fields.Many2one(comodel_name='subject.details',string="Subject")                  # ids_name = fields.Many2one('relation_model_name',string='',ondelete='cascade')
	add_subject_ids = fields.One2many('subject.details','details_id',string="Subject Options")      # ids_name = fields.One2many('relation_model_name','inverse_name',string='')

	# subject_ids = fields.Many2many(string="Subjects",'subject.details')      # ids_name = fields.One2many('relation_model_name','inverse_name',string='')


	# @api.onchange('base_price','additional_fee')  # invoke when wenchange in  "additional_fee"  and "base_price", we also can changes in total_price
	# def _onchange_total_price(self):
	# 	print("ssssssssssssssssssssss",self.base_price)
	# 	if self.base_price<0.00:
	# 		raise UserError('base price cannot be set as nagative')

	# 	self.total_price=self.base_price+self.additional_fee

	@api.depends('base_price','additional_fee') # invoke when we  change in  "additional_fee"  and "base_price" and we can't changes in total_price due to @api.depends 
	def _compute_total_price(self):
		print("base_price------------------>",self.base_price)
		if self.base_price < 0.0:
			raise UserError('base price cannot be set as nagative')

		self.total_price = self.base_price +  self.additional_fee


	# @api.ondelete(at_uninstall=False)
	# def _check_active(self):
	# 	for rec2 in self:
	# 		if rec2.active:  #you can't delete this appointment if datetime is assing
	# 			raise UserError("You can't delete this record")




	@api.depends('lecture_starttime','duration') # everytime when we  change in  "lecture_starttime"  and "duration" this will update in enddate 
	def _compute_lecture_endtime(self):
		for record in self:
			if not (record.lecture_starttime and record.duration):
				record.lecture_endtime =record.lecture_starttime
			else:
				duration=timedelta(days=record.duration)  # timedelta use of calculate a duration in time instaed of int value 
				record.lecture_endtime=record.lecture_starttime+duration


	def _inverse_lecture_endtime(self):
		for record in self:
			if  record.lecture_starttime and record.duration:
				record.duration =(record.lecture_endtime  - record.lecture_starttime).days+1
			else:
				continue 
		



	@api.onchange('additional_fee') # invoke when we  change in  "additional_fee" 
	def _check_additional_fee(self):
		for record in self:
			print('self ------------------>',record)
			if record.additional_fee<10.00:
				raise ValidationError('additional_fee cannot be less than 10: %s'%record.additional_fee)

	# @api.model
	# def create(self,vals): # invoke when we click on create+save button 
	# 	print("create  method------------------>",vals)
	# 	if vals.get('name') == 'meet':
	# 		vals['name'] = 'Riddhi'
	# 	res = super(Course,self).create(vals)
	# 	return res
	# 	# super(classname,self).craete(other parameer which given in sheet)

	
	# def write(self,vals):  #no decorators needed for  write method  invoke when we click on Edit+save button
	# 	print("write method------------------>",vals)
	# 	if vals.get('name') == 'meet':
	# 		vals['name'] = 'Meet'
	# 	res = super(Course,self).write(vals)
	# 	return res

	# @api.constrains('description')
	# def check_description(self):
	# 	for rec in self:
	# 		note=self.env['academy.course'].search([('description', '=', rec.description)])
	# 		if note:
	# 			raise ValidationError("description is  %s already exists",rec.description)




	@api.onchange('base_price','additional_fee')  # invoke when we  change in  "additional_fee"  and "base_price" and we can changes in total_price
	def _onchange_total_price(self):
		browse_method=self.env['academy.course'].browse([3,2,1]) #browse(3) when we provide single record id
		
		print('-------------------------------------->>>',browse_method) #browse_method=academy.course(15, 14, 1)

		for i in browse_method: # i=academy.course(1,) ,i=academy.course(15,),i=academy.course(14,) 
			print(i.additional_fee)  

		# search_method=self.env['academy.course'].search([('partner_id', '=', seller.id)])


	@api.onchange('name')
	def _onchange_name(self):

		#search method
		courses=self.env['academy.course'].search([]) 
		print(courses) #it(empty domain) will return all recordset ex- courses=academy.course(1, 2, 3)

		#search "AND" condition
		price_check=self.env['academy.course'].search([('base_price','<=','100'),('additional_fee','=','10')]) #if we changes in any record name 
		print('base_price_check is',price_check)#base_price_check is academy.course(1, 2)


		#search "OR" condition
		price_check=self.env['academy.course'].search(['|',('base_price','<','100'),('additional_fee','=','10')]) #if we changes in any record name 
		print('base_price_check is',price_check)#base_price_check is academy.course(1, 2,3)



		#search_count method
		Beginner_course=self.env['academy.course'].search_count([('level','=','beginner')]) 
		print('Beginner_course is',Beginner_course)#Beginner_courses where level is beginner "number of record"


		#ref method

		# course_id=self.env['Odoo___Academy.course_view_form'] #External ID of view "modulename.templateid"
		# print('course_id is ',course_id) #record object of this view  if you print "course_id.id" it will be return a id of record


		#browse method

		#browse_method1=self.env['academy.course'].browse([3,2,1]) #browse(3) when we provide single record id
		# print(browse_method1)


		#exists method   #it use  for checking a given recordid is exists or not

		browse_method2=self.env['academy.course'].browse(1) #browse(3) when we provide single record id
		if browse_method2.exists():
			print(browse_method2,"recordID is exists")
		else:
			print("not exists")


		#create method #it is use for craete a record 

		vals={'name':"accounting","description":"description using craete method"} 
		self.env['academy.course'].create(vals)

		vals={'name':"accounting","description":"description using craete method"} 
		new_record=self.env['academy.course'].create(vals)	
		print('new_record is ',new_record,new_record.id) # new_record=academy.course(10,), new_record.id=10


		#write method use for edit a record

		record_update=browse_method2=self.env['academy.course'].browse(1)
		if record_update.exists():
			vals1={'name':"HTML course","description":"description using Edit method"}
			record_update.write(vals1)


		#copy method use for craete duplicate record
		# copy_this_record=browse_method2=self.env['academy.course'].browse(3)
		# copy_this_record.copy()




        
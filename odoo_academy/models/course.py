
from pickle import TRUE
import string
from odoo import models, fields, api
from odoo.exceptions import UserError, ValidationError


class Course(models.Model):

    _name = "course.academy"
    _description = "Course Info"
    
    
    name = fields.Char(string="Title")
    description = fields.Text(string="Description",help="Enter Description",readonly=False)

    level = fields.Selection(string="Level",
                selection = [("beginner","Beginner"),("intermediate","Intermediate"),("advanced","Advanced")],default='advanced')

    active = fields.Boolean(string="Active", default=True)

    base_price = fields.Float(string="Base price", default=0.00)
    additional_fee = fields.Float(string="additional fee", default = 0.00)
    total_price = fields.Float(string="total price", readonly = True)

    @api.onchange('base_price', 'additional_fee')
    def _onchange_total_price(self):
        if self.base_price < 0.00:
            raise UserError('Base price cannot be set as negative. ')
        self.total_price = self.base_price + self.additional_fee

    @api.constrains('additional_fee')
    def _check_additional_fee(self):
        for record in self:
                if record.additional_fee < 10.00:
                    raise ValidationError('Additional fee cannot be less than 10.00: %s' % record.additional_fee)

    #end_course_date = fields.Datetime(string='End Date')
    #start_course_date = fields.Date(string='Start Date')
    


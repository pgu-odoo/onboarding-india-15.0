# -*- coding: utf -8 -*-

from odoo import fields,models,api

class Passengers(models.Model):

    #CLASS ATTRIBUTES
    _name = 'railway.passenger'
    _description = 'Railway Management Software'
    _auto  = True

    #SIMPLE FIELDS
    seat_no = fields.Integer(string='Seat No.')
    name = fields.Char(string="Passengers_Name",required=True, placeholder="Enter Passenger Name E.g Suresh Chavda")
    gender = fields.Selection([('male', 'Male'), ('female', 'Female'), ('other', 'Other')])
    age = fields.Integer(string='Age')
    completed = fields.Boolean(string='Journey Completed?')
    source = fields.Char(string='Source Station')
    destination = fields.Char(string='Destination Station')
    date_of_journey = fields.Datetime(string='Date of Journey')
    Class = fields.Selection([('1stAC','1st AC'), ('2ndAC','2nd AC'),
                              ('3rdAC','3rd AC'), ('sleeper','sleeper'),('general','General')],default='general')

    #RELATIONAL FIELDS
    # ticket_fare = fields.One2many(comodel_name="railway.fare",string='Journey Fare')



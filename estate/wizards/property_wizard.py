# -*- coding: utf-8 -*-
from attr import field
from odoo import models, fields, api

class property_wizard(models.TransientModel):
    _name = "property.wizard"
    _description = "Property wizard"
    
    price = fields.Char()
    partner_id = fields.Many2one('res.partner', 'Name')   

    def action_add_offer(self):
        self.ensure_one()
        activeIds = self.env.context.get('active_ids')
        for x in activeIds:
            self.env['estate.property.offer'].create({'price':self.price ,'partner_id': self.partner_id.id,'property_id':x})
        return True

class TagWizard(models.TransientModel):
    _name = "tag.wizard"
    _description = "Tag Wizard"

    tag_id = fields.Many2many('estate.property.tag')

    def action_add_tag(self):
        self.ensure_one()
        #it ensures that only one record is passed at a time so system will not throw up an error.

        activeIds = self.env.context.get('active_ids')

        for x in activeIds:
            a = self.env['estate.property'].browse(x)
            # print("#######################################",a.property_tag_ids + self.tag_id)
            self.env['estate.property'].browse(x).write({'property_tag_ids': a.property_tag_ids + self.tag_id})
        return True
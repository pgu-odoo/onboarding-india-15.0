# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import models, fields, api, _


class LoyaltyProgramRanking(models.Model):
    _name = 'loyalty.program.ranking'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string='Name', index=True, required=True)
    user_id = fields.Many2one('res.users', string='Responsible')
    active = fields.Boolean('Active', default=False, tracking=True)
    rank_type = fields.Selection([
        ('silver', 'Silver'),
        ('gold', 'Gold')], 'Ranking Type')
    starting_points = fields.Float('Starting Points')

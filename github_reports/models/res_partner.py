# -*- coding: utf-8 -*-

from odoo import api, fields, models
import requests
import json
from datetime import datetime


class ResPartner(models.Model):
    _inherit = "res.partner"
    
    github_user = fields.Char()
    contributions = fields.One2many('pr.comment', 'contributor')
    pull_requests = fields.One2many('pull.request', 'author')
    contribution_count = fields.Integer(compute='_compute_contribution')
    pr_count = fields.Integer("PR Count", compute='_compute_pr')

    def action_view_partner_contribution(self):
        self.ensure_one()
        action = self.env['ir.actions.actions']._for_xml_id("github_reports.pr_comment_action")
        action['domain'] = [('contributor', '=', self.id)]
        return action

    def action_view_partner_pull_requests(self):
        self.ensure_one()
        action = self.env["ir.actions.actions"]._for_xml_id("github_reports.pull_request_action")
        action['domain'] = [('author', '=', self.id)]
        return action

    @api.depends('contributions')
    def _compute_contribution(self):
        for p in self:
            p.contribution_count = len(p.contributions)

    @api.depends('pull_requests')
    def _compute_pr(self):
        for p in self:
            p.pr_count = len(p.pull_requests)

    
    def cron_fetch(self):
        self.search([('github_id','!=', False),('fetch_issues','=', True)]).fetch_pr()
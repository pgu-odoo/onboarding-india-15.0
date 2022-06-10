# -*- coding: utf-8 -*-

import requests
import json

from odoo import fields, models, _
from datetime import datetime
from odoo.exceptions import UserError


class PullRequest(models.Model):
    _name = "pull.request"
    _description = "Pull Request"
    _rec_name = 'pr_number'

    git_id = fields.Char()
    pr_number = fields.Char()
    title = fields.Char()
    state = fields.Selection([
        ('draft', 'Draft'),
        ('open', 'Open'),
        ('closed', 'Closed')], default='draft')
    body = fields.Char()
    draft = fields.Boolean()
    create_date = fields.Datetime()
    closed_date = fields.Datetime()
    author = fields.Many2one('res.partner')
    team = fields.Many2one('github.team')
    comments = fields.One2many('pr.comment','pr')
    
        
    def fetch_comments(self):
        session = requests.Session()

        for pr in self:

            url = f"https://api.github.com/repos/odoo/odoo/issues/{pr.pr_number}/comments"
            session.auth = (pr.git_id, pr.team.github_user)
            
            try:
                response = session.get(url)
                response.raise_for_status()
            except UserError as e:
                return e
            
            for comment in response.json():
                created_date = datetime.strptime(comment.get('created_at'), "%Y-%m-%dT%H:%M:%SZ").strftime("%Y-%m-%d %H:%M")
                updated_date = datetime.strptime(comment.get('updated_at'), "%Y-%m-%dT%H:%M:%SZ").strftime("%Y-%m-%d %H:%M")                
                contributor = self.env['res.partner'].search([('github_user', '=', comment.get('user').get("login"))])
                pr_comment = self.env['pr.comment'].search([('git_id', '=', str(comment['id']))])
                if pr_comment:
                    if pr_comment.updated_date.strftime("%Y-%m-%d %H:%M") != updated_date:
                        pr_comment.write({
                            'body': comment.get('body'),
                            'updated_date': updated_date,
                        })
                else:
                    self.env['pr.comment'].create({
                        'pr': pr.id,
                        'git_id': comment.get('id'),
                        'body': comment.get('body'),
                        'contributor': contributor and contributor.id,
                        'created_date': created_date,
                        'updated_date': updated_date,
                    })



class PullRequestComment(models.Model):
    _name = "pr.comment"
    _description = "PR Comments"
    _rec_name = 'pr'
    
    pr = fields.Many2one('pull.request', ondelete='cascade')
    contributor = fields.Many2one('res.partner')
    body = fields.Char()
    git_id = fields.Char()
    created_date = fields.Datetime()
    updated_date = fields.Datetime()

       
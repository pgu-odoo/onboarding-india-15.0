# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models, _


class LunchOrder(models.Model):
    _name = 'lunch.order'
    _description = 'Lunch order'

    name = fields.Char(string='Order Reference', required=True, copy=False, readonly=True, states={'draft': [('readonly', False)]}, index=True, default=lambda self: _('New'))
    state = fields.Selection([
        ('draft', 'Draft'),
        ('done', 'Done'),
        ], string='Status', readonly=True, default='draft') 
    date_order = fields.Datetime(string='Order Date', default=fields.Datetime.now, help="Creation date of draft/sent orders")
    order_lines = fields.One2many('lunch.order.line', 'order_id', string='Order Lines', auto_join=True)
    partner_id = fields.Many2one('res.partner', string='Customer')

class LunchOrderLine(models.Model):
    _name = 'lunch.order.line'
    _description = 'Lunch order line'

    order_id = fields.Many2one('lunch.order', string='Order Reference', required=True, ondelete='cascade')
    name = fields.Text(string='Description')
    product_id = fields.Many2one('product.product', string='Product', domain="[('lunch_ok', '=', True)")
    product_uom_qty = fields.Float(string='Quantity', digits='Product Unit of Measure', default=1.0)
    price = fields.Float(string='Quantity', digits='Product Unit of Measure', default=1.0)
from odoo import fields, models, _


class ShopOrder(models.Model):
    _name = 'shop.order'
    _description = 'Shop Order'

    name = fields.Char(string='Order Reference', required=True, copy=False, readonly=True,
                                                 states={'draft': [('readonly', False)]},
                                                 index=True,
                                                 default=lambda self: _('New'))
    state = fields.Selection([('draft', 'Draft'),
                              ('done', 'Done')], string='Status', readonly=True, default='draft')
    order_date = fields.Datetime(string="Order Date", default=fields.Datetime.now, help="Creation date of draft/sent orders")
    order_lines = fields.One2many("shop.order.line", "order_id", string="order Lines", auto_join=True)
    partner_id = fields.Many2one('res.partner', string="Customer")


class ShopOrderLine(models.Model):
    _name = 'shop.order.line'
    _description = 'Shop Order Line'

    order_id = fields.Many2one("shop.order", string="Order Reference", required=True, ondelete='cascade')

    name = fields.Text(string="Description")
    product_id = fields.Many2one("product.product", string="Product", domain="[('check', '=', True)]")
    product_uom_type = fields.Float(string="Quantity", digits="Product UoM", default=1.0)
    price = fields.Float(string="Price", digits="Product UoM", default=1.0)

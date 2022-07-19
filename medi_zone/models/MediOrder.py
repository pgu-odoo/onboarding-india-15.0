from odoo import fields, models, _

class MediOrder(models.Model):
	_name = 'medi.order'
	_description = 'Medi order'

	name = fields.Char(string='Order Reference', required=True, copy=False, readonly=True, states={'draft': [('readonly', False)]}, index=True, default=lambda self:_('New'))

	state = fields.Selection([
		('draft','Draft'),
		('done','Done'),
		], string='Status', readonly=True, default='draft')
	date_order = fields.Datetime(string='Order Date', default=fields.Datetime.now, help="Create date of draft/sent orders")

	order_lines = fields.One2many('medi.order.line', 'order_id', string='Order Lines', auto_join=True)

	partner_id = fields.Many2one('res.partner', string="Customer")

class MediOrderLines(models.Model):
	_name = 'medi.order.line'

	_description = 'Medi order line'

	order_id = fields.Many2one('medi.order', string='Order Reference', required=True, ondelete='cascade')
	name = fields.Text(string='Description')

	product_id = fields.Many2one('product.template' ,string='Product', domain="[('medi_ok', '=', True)]")

	product_uom_qty = fields.Float(string='Quantity', digits='Product Unit of Measure', default=1.0)

	price = fields.Float(string='Price', digits='Product Unit of Measure', default=1.0)
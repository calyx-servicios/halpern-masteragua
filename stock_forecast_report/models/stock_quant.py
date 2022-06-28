from odoo import api, fields, models, _
from odoo.exceptions import ValidationError
from odoo.addons import decimal_precision as dp
from odoo.tools.float_utils import float_round


class StockQuant(models.Model):
    _inherit = 'stock.quant'

    product_id = fields.Many2one(
        'product.product', 'Product',
        ondelete='restrict', readonly=True, required=True, index=True)

    quantity = fields.Float(
        'Quantity',
        readonly=True)

    open_sales_orders = fields.Float(
        'OV comp',
        readonly=True,
        related="product_id.sales_count")

    open_purchase_orders = fields.Float(
        'OC comp',
        readonly=True,
        related="product_id.purchased_product_qty")

    lead_time = fields.Float(
        'Lead Time',
        readonly=True,
        related="product_id.sale_delay")

    qty_available_ = fields.Float(
        string="Quantity Available",
        compute="_compute_qty_available",
    )

    analytic_account_id = fields.Char(
        'Analytic Account', 
        readonly=True)

    purchased_product_qty = fields.Float(string='Purchased')

    product_uom_qty = fields.Float(
        'Initial Demand',
        digits=dp.get_precision('Product Unit of Measure'),
        default=0.0, required=True, states={'done': [('readonly', True)]},
        help="This is the quantity of products from an inventory "
             "point of view. For moves in the state 'done', this is the "
             "quantity of products that were actually moved. For other "
             "moves, this is the quantity of product that is planned to "
             "be moved. Lowering this quantity does not generate a "
             "backorder. Changing this quantity on assigned moves affects "
             "the product reservation, and should be done with care.")

    def _compute_qty_available(self):
        for rec in self:
            rec.qty_available_ = rec.product_id.with_context(
                {'location': rec.location_id.id}).qty_available_

    @api.depends('quantity','open_sales_orders','open_purchase_orders') 
    def _compute_purchase_request(self):
        for rec in self:
            rec.purchase_request = rec.quantity - rec.open_sales_orders + rec.open_purchase_orders

    purchase_request = fields.Float(
        'Purch Req',
        readonly=True,
        compute="_compute_purchase_request")

    @api.depends('planned_quantity','open_sales_orders') 
    def _compute_total(self):
        for rec in self:
            rec.total = rec.planned_quantity - rec.open_sales_orders
    
    total = fields.Float(
        'Total',
        readonly=True,
        compute="_compute_total")

    @api.depends('quantity','open_purchase_orders','purchase_request') 
    def _compute_planned_quantity(self):
        for rec in self:
            rec.planned_quantity = rec.quantity + rec.open_purchase_orders + rec.purchase_request

    planned_quantity = fields.Float(
        'Planned Quantity',
        readonly=True,
        compute="_compute_planned_quantity")

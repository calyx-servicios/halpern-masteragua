from odoo import api, fields, models, _
from odoo.exceptions import UserError, ValidationError


class StockQuant(models.Model):
    _inherit = 'stock.quant'

    product_id = fields.Many2one(
        'product.product', 'Product',
        ondelete='restrict', readonly=True, required=True, index=True)

    quantity_on_hand = fields.Float(
        'Quantity',
        help='Quantity of products in this quant, in the default unit of measure of the product',
        oldname='qty', readonly=True)

    quantity = fields.Float(
        'Quantity',
        readonly=True)

    open_sales_orders = fields.Float(
        'OV comp',
        readonly=True)

    open_purchase_orders = fields.Float(
        'OC comp',
        readonly=True)

    lead_time = fields.Float(
        'Lead Time',
        readonly=True)

    purchase_request = fields.Float(
        'Purch Req',
        readonly=True)
    
    total = fields.Float(
        'Total',
        readonly=True)


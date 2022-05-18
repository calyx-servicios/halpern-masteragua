# -*- coding: utf-8 -*-

from odoo import api, fields, models

class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    categ_id = fields.Many2one(related="product_id.categ_id")
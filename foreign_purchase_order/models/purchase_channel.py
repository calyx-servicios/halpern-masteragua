from odoo import models, fields, api


class PurchaseChannel(models.Model):
    _name="purchase.channel"

    name = fields.Char(string="Channel")
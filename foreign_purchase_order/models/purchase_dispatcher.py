from odoo import models,fields,api


class PurchaseDispatcher(models.Model):
    _name="purchase.dispatcher"

    name = fields.Char(String="Name")
    address = fields.Char(string="Address")
    email = fields.Char(string="Email")
    phone = fields.Char(string="Phone")
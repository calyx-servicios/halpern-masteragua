from odoo import models,fields,api


class PurchaseBooking(models.Model):
    _name="purchase.booking"


    name = fields.Char(string="Transportation Mean")
    
from odoo import fields, models


class ProductTemplate(models.Model):
    _inherit = "product.template"

    tango_reference = fields.Char("Tango Reference", index=True, size=100)

from odoo import api, fields, models, _
from odoo.exceptions import UserError, ValidationError


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    tango_reference = fields.Char('Tango Reference', index=True, size=100)

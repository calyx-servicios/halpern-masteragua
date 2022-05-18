# -*- coding: utf-8 -*-

from odoo import models, api, fields

class Project(models.Model):
    _inherit = "project.project"

    place = fields.Char('Place')
    seller = fields.Char('Seller')
    cultivation = fields.Char('Cultivation')
    risk_system = fields.Char('Risk System')
    hectare = fields.Char('Hectare')
    ditch = fields.Char('Ditch')
    proforma_number = fields.Char('Proforma Number')
    contact = fields.Char('Contact')
    observations = fields.Char('Observations')


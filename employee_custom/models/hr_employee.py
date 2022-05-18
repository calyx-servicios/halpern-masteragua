# -*- coding: utf-8 -*-

from odoo import models, api, fields

class Project(models.Model):
    _inherit = "hr.employee"

    location = fields.Char('Location')
    collective_agreements = fields.Char('Collective agreements')
    gross_salary = fields.Char('Gross salary')
    children_name = fields.Char('Children')
    date_birth = fields.Date('Date of birth')
    Last_name = fields.Char('Last name and name')

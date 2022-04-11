# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ResPartnertInherit(models.Model):
    _inherit = 'res.partner'

    fax = fields.Char(string="Fax")
    ice = fields.Char(string="ICE")


class ResCompanyInherit(models.Model):
    _inherit = 'res.company'

    fax = fields.Char(string="Fax")
    ice = fields.Char(string="ICE")
    cnss = fields.Char(string="CNSS")
    if_fiscal = fields.Char(string="IF")


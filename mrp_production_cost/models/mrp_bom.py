# -*- coding: utf-8 -*-
# Copyright 2017 valentin vinagre <valentin.vinagre@qubiq.es>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl)

from odoo import models, fields, _


class MrpBom(models.Model):
    _inherit = 'mrp.bom'

    cost_production = fields.Float(string=_('Labour cost'), default=0.0)

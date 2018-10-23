# Copyright 2018 <oscar.navarro@qubiq.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import models, fields, api, _


class MrpBom(models.Model):
    _inherit = 'mrp.bom'

    qty_available = fields.Float(
        related='product_tmpl_id.qty_available',
        string=_('Quantity On Hand'),
        readonly=True,
        store=True
    )

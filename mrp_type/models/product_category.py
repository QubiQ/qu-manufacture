# Copyright 2018 Xavier Piernas <xavier.piernas@qubiq.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).


from odoo import models, fields, _


class ProductCategory(models.Model):
    _inherit = 'product.category'

    mrp_type = fields.Many2one(
        comodel_name='mrp.type',
        string=_('MRP Type')
    )

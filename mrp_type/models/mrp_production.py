# Copyright 2018 Xavier Piernas <xavier.piernas@qubiq.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).


from odoo import models, fields, api, _


class MrpProduction(models.Model):
    _inherit = 'mrp.production'

    mrp_type = fields.Many2one(
        comodel_name='mrp.type',
        string=_('MRP Type')
    )

    @api.model
    def create(self, values):
        if 'mrp_type' in values and values['mrp_type']:
            values.update({
                'name': self.env['mrp.type'].browse(
                    values['mrp_type']
                ).sequence_id._next() or _('New')
            })
        return super(MrpProduction, self).create(values)

    @api.onchange('product_id')
    def _onchange_product_id(self):
        mrp_type = False
        if self.product_id:
            mrp_type = self.env['product.product'].\
                get_mrp_type(self.product_id)
        self.mrp_type = mrp_type

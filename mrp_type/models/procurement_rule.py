# Copyright 2018 Xavier Piernas <xavier.piernas@qubiq.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).


from odoo import models


class ProcurementRule(models.Model):
    _inherit = 'procurement.rule'

    def _prepare_mo_vals(
        self, product_id, product_qty, product_uom, location_id, name, origin,
        values, bom
    ):
        res = super(ProcurementRule, self)._prepare_mo_vals(
            product_id, product_qty, product_uom, location_id, name, origin,
            values, bom
        )
        res.update({
            'mrp_type': self.env['product.product'].get_mrp_type(product_id)
        })
        return res

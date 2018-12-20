# Copyright 2018 Xavier Piernas <xavier.piernas@qubiq.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).


from odoo import models


class ProductProduct(models.Model):
    _inherit = 'product.product'

    def get_mrp_type(self, product_id):
        mrp_type = False
        if product_id.categ_id.mrp_type:
            mrp_type = product_id.categ_id.mrp_type.id
        else:
            categ_id = product_id.categ_id.parent_id
            while categ_id and not mrp_type:
                if categ_id.mrp_type:
                    mrp_type = categ_id.mrp_type.id
                categ_id = categ_id.parent_id
        return mrp_type

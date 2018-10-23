# Copyright 2018 <oscar.navarro@qubiq.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import models, fields, api, _

class product_product(models.Model):
    _inherit = 'product.product'

    stock_assembled = fields.Integer(
        string=_("Stock assembled"),
        compute='_getAssembledStock',
        help=_('Stock assembled in kits (need to be dissasembled' +
               'for availablity)')
    )
    num_proveedor = fields.Char(
        string=_("Internal Provider Code")
    )
    available_qty_general = fields.Float(
        string=_("Avaible Stock"),
        compute="_get_available_qty_general"
    )

    @api.multi
    def _getAssembledStock(self):
        # Busca kits que no esten reservados que no tengan el producto.
        for element in self:
            total = 0

            for line in self.env['mrp.bom.line'].search([(
                'product_id', '=', element.id)]
               ).filtered(lambda x: x.bom_id.product_tmpl_id.qty_available > 0):
                    total += line.product_qty *\
                        line.bom_id.product_tmpl_id.qty_available
            element.stock_assembled = total

    # Function to calculate the qty available only on GENERAL warehouse
    @api.multi
    def _get_available_qty_general(self):
        # Get qty available on GENERAL for each product
        for product in self:
            product.available_qty_general = product.with_context({
                'warehouse': 1}).qty_available

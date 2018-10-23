# Copyright 2018 <oscar.navarro@qubiq.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import models, fields, api, _


class product_template(models.Model):
    _inherit = 'product.template'

    stock_assembled = fields.Integer(
        string=_("Stock assembled"),
        compute='_getAssembledStock',
        help=_('Stock assembled in kits ' +
               '(need to be dissasambled for availablity)')
    )
    stock_assembled_text = fields.Char(
        string=_("Stock Assembled"),
        compute='_getAssembledStockText'
    )
    num_proveedor = fields.Char(
        string=_("Internal Provider Code")
    )

    @api.multi
    def _getAssembledStockText(self):
        for el in self:
            el.stock_assembled_text = str(el.stock_assembled)

    @api.multi
    def _getAssembledStock(self):
        """
         Compute the potential as the max of all the variants's potential.

        We can't add the potential of variants: if they share components we
        may not be able to make all the variants.
        So we set the arbitrary rule that we can promise up to the biggest
        variant's potential.

        Busca kits que no esten reservados que contengan el producto.
        """
        for tmpl in self:
            if not tmpl.product_variant_ids:
                continue
            tmpl.stock_assembled = max(
                [v.stock_assembled for v in tmpl.product_variant_ids])

    @api.multi
    def action_view_kits(self):
        action = self.env.ref('mrp.product_open_bom').read()[0]
        if self.product_variant_ids:
            id_max = 0
            max_qty = 0
            for variant in self.product_variant_ids:
                if variant.stock_assembled > max_qty:
                    max_qty = variant.stock_assembled_text
                    id_max = variant.id
            action['context'] = {
                'default_component_id': id_max,
            }
            domain = [('bom_line_ids.product_id', 'in', [id_max]), ]
            view_id = self.env.ref('assembled_stock.view_assembled_stock_tree').id
            if view_id:
                return {
                        'type': 'ir.actions.act_window',
                        'name': _('Bill of Materials'),
                        'res_model': 'mrp.bom',
                        'target': 'current',
                        'domain': domain,
                        'view_type': 'form',
                        'view_mode': 'tree',
                        'views': [[view_id, 'list']],
                        }

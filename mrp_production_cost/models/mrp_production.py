# -*- coding: utf-8 -*-
# Copyright 2017 valentin vinagre <valentin.vinagre@qubiq.es>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl)

from odoo import models, fields, api, SUPERUSER_ID, _


class MrpProduction(models.Model):
    _inherit = 'mrp.production'

    recalculate_cost = fields.Boolean(
        string=_("Recalculate cost"), default=False)
    cost_production = fields.Float(string=_('Labour cost'), default=0.0)
    cost_all_production = fields.Float(
        string=_("Cost manufacturing"),
        readonly=True,
        compute='_get_cost_all_production'
        )

    @api.model
    def create(self, values):
        values['cost_production'] = self.env['mrp.bom'].\
            browse(values['bom_id'])[0].cost_production or 0.0
        return super(MrpProduction, self).create(values)

    @api.multi
    @api.onchange('bom_id')
    def onchange_bom_id(self):
        for sel in self:
            sel.cost_production = sel.bom_id.cost_production or 0.0

    @api.multi
    def button_recalculate_cost(self):
        for sel in self.env(user=SUPERUSER_ID)['mrp.production'].browse(
            self.ids
           ):
            if sel.recalculate_cost and sel.state == 'done':
                unit_price = sel.cost_all_production/sel.product_qty
                for move_finish in sel.move_finished_ids:
                    for quant in move_finish.quant_ids:
                        quant.cost = unit_price
                sel.recalculate_cost = False

    @api.multi
    def button_mark_done(self):
        res = super(MrpProduction, self).button_mark_done()
        if self.state == 'done':
            unit_price = self.cost_all_production/self.product_qty
            for move_finish in self.env(user=SUPERUSER_ID)['mrp.production'].\
                    browse(self.ids).move_finished_ids:
                for quant in move_finish.quant_ids:
                    quant.cost = unit_price
        return res

    @api.multi
    def _get_cost_all_production(self):
        for sel in self:
            total = sel.cost_production * sel.product_qty
            for move in sel.move_raw_ids:
                total_aux = 0.0
                for quant in move.quant_ids:
                    total_aux += quant.inventory_value
                if total_aux == 0.0:
                    total_aux +=\
                        move.product_id.standard_price * move.product_uom_qty
                total += total_aux
            sel.cost_all_production = total

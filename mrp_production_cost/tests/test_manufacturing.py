# -*- coding: utf-8 -*-
# Copyright 2017 valentin vinagre <valentin.vinagre@qubiq.es>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl)

from odoo.tests.common import TransactionCase


class TestManufacturing(TransactionCase):

    def setUp(self):
        super(TestManufacturing, self).setUp()
        self.product_product = self.env['product.product']
        self.mrp_bom = self.env['mrp.brom']
        self.mrp_production = self.env['mrp.production']
        self.uom_unit = self.env.ref('product.product_uom_unit')
        self.manufacture_route = self.env.ref(
            'mrp.route_warehouse0_manufacture')
        self.product_manuf = self.product_product.create({
            'name': 'Manuf',
            'type': 'product',
            'uom_id': self.uom_unit.id,
            'standard_price': 0.20,
            'route_ids': [(4, self.manufacture_route.id)]
            })
        self.product_material_first = self.product_product.create({
            'name': 'Material',
            'type': 'product',
            'uom_id': self.uom_unit.id,
            'standard_price': 0.10,
            })
        self.bom = self.env['mrp.bom'].create({
            'product_id': self.product_manuf.id,
            'product_tmpl_id': self.product_manuf.product_tmpl_id.id,
            'cost_production': 2.0,
            'bom_line_ids': ([
                (0, 0, {
                    'product_id': self.product_material_first.id,
                    'product_qty': 1,
                    'product_uom_id': self.uom_unit.id
                }),
            ])
        })
        self.bom_2 = self.env['mrp.bom'].create({
            'product_id': self.product_manuf.id,
            'product_tmpl_id': self.product_manuf.product_tmpl_id.id,
            'cost_production': 2.0,
            'bom_line_ids': ([
                (0, 0, {
                    'product_id': self.product_material_first.id,
                    'product_qty': 2,
                    'product_uom_id': self.uom_unit.id
                }),
            ])
        })

    def test_manufacture_bom(self):
        production = self.mrp_production.create({
            'product_id': self.product_manuf.id,
            'product_qty': 1,
            'product_uom_id': self.uom_unit.id,
            'bom_id': self.bom.id,
            })
        self.assertEqual(production.cost_production, 2.0)
        self.assertEqual(production.cost_all_production, 2.1)

    def test_manufacture_bom_change_qty(self):
        production = self.mrp_production.create({
            'product_id': self.product_manuf.id,
            'product_qty': 2,
            'product_uom_id': self.uom_unit.id,
            'bom_id': self.bom.id,
            })
        self.assertEqual(production.cost_production, 2.0)
        self.assertEqual(production.cost_all_production, 4.2)

    def test_manufacture_bom_2(self):
        production = self.mrp_production.create({
            'product_id': self.product_manuf.id,
            'product_qty': 1,
            'product_uom_id': self.uom_unit.id,
            'bom_id': self.bom_2.id,
            })
        self.assertEqual(production.cost_production, 2.0)
        self.assertEqual(production.cost_all_production, 2.2)

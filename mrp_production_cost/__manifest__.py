# -*- coding: utf-8 -*-
# Copyright 2017 valentin vinagre <valentin.vinagre@qubiq.es>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl)

{
    "name": "Mrp production cost",
    "version": "10.0.1.0.0",
    "author": "QubiQ, Odoo Community Association (OCA)",
    "website": "https://www.qubiq.es",
    "category": "Manufacturing",
    "license": "AGPL-3",
    "depends": [
        "base",
        "mrp",
    ],
    "data": [
        "views/mrp_bom.xml",
        "views/mrp_production.xml",
    ],
    'installable': True,
    'application': False,
}

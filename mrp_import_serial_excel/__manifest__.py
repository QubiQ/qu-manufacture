# -*- coding: utf-8 -*-
# © 2018 Xavier Jiménez <xavier.jimenez@qubiq.es>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    "name": "MRP Import Serial Number Excel",
    "version": "10.0.1.0.0",
    "author": "QubiQ",
    "website": "https://www.qubiq.es",
    "category": "MRP",
    "license": "AGPL-3",
    "depends": [
        "base",
        "product",
        "stock",
        "mrp",
    ],
    "data": [
        'views/mrp_production_view.xml',
    ],
    "external_dependencies": {
        "python": [],
        "bin": [],
    },
    'installable': True,
    'application': False,
}

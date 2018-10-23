# Copyright 2018 <oscar.navarro@qubiq.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

{
    "name": "Assembled Stock",
    "summary": "This module adds an information box to materials about their produced products.",
    "version": "11.0.1.0.0",
    "author": "QubiQ, Odoo Community Association (OCA)",
    "license": "AGPL-3",
    "application": False,
    "installable": True,
    "depends": [
        "product",
        "stock",
        "mrp",
    ],
    "data": [
        "views/product_template_view.xml",
    ],
}

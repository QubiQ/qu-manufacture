# Copyright 2018 Xavier Piernas <xavier.piernas@qubiq.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

{
    "name": "MRP Type",
    "summary": "MRP Type on Manufacturing Orders",
    "version": "11.0.1.0.0",
    "category": "MRP",
    "website": "https://www.qubiq.es",
    "author": "QubiQ, Odoo Community Association (OCA)",
    "license": "AGPL-3",
    "application": False,
    "installable": True,
    "depends": [
        "mrp",
        "product",
        "sales_team"
    ],
    "data": [
        "security/ir.model.access.csv",
        "views/mrp_type.xml",
        "views/mrp_production.xml",
        "views/product_category.xml"
    ],
}

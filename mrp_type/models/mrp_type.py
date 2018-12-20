# Copyright 2018 Xavier Piernas <xavier.piernas@qubiq.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).


from odoo import models, fields, _


class MrpType(models.Model):
    _name = 'mrp.type'

    name = fields.Char(
        string=_('Name'),
        required=True
    )
    company_id = fields.Many2one(
        comodel_name='res.company',
        default=lambda self: self.env.user.company_id,
        string=_('Company'),
        readonly=True
    )
    sequence_id = fields.Many2one(
        comodel_name='ir.sequence',
        string=_('Sequence'),
        required=True
    )

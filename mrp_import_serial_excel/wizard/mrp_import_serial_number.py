# -*- coding: utf-8 -*-
# © 2018 Xavier Jiménez <xavier.jimenez@qubiq.es>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, fields, models, _
from odoo.exceptions import ValidationError
import tempfile
import binascii
import xlrd

import logging
_logger = logging.getLogger(__name__)


class MrpImportSerialNumber(models.TransientModel):
    _name = 'mrp.import.serial.number'

    data = fields.Binary(
        'File',
        required=True,
    )
    name = fields.Char(
        'Filename',
    )

    '''
        Function to import the serial numbers and complete the mrp
    '''
    @api.multi
    def import_serial_numbers(self, serials_dict, notes_dict):
        mrp_obj = self.env['mrp.production'].browse(
            self._context.get('active_id'))

        # Delete all the serials that Odoo assigns by default
        for raw in mrp_obj.move_raw_ids:
            if raw.product_id.tracking == 'serial':
                raw.active_move_lot_ids = [(5,)]

        # Assign serial numbers to the final product
        for finished in mrp_obj.move_finished_ids:
            if finished.product_id.tracking == 'serial':
                serials_numbers = serials_dict[finished.product_id.name]
                # Delete previous assigned serials
                finished.active_move_lot_ids = [(5,)]
                # For each serial, assign materials after creating the lot
                for serial in serials_numbers:
                    fin_lot_obj = self.env['stock.production.lot'].search([(
                        'name', '=', serial)])
                    if not fin_lot_obj:
                        fin_lot_obj = fin_lot_obj.create({
                            'name': serial,
                            'product_id': finished.product_id.id,
                            'product_qty': 1,
                            'internal_notes': notes_dict[serial],
                        })
                    finished.active_move_lot_ids = [(0, 0, {
                        'lot_id': fin_lot_obj.id,
                        'quantity_done': 1,
                        'production_id': mrp_obj.id,
                    })]
                    # Assign serial numbers to materials
                    for raw in mrp_obj.move_raw_ids:
                        if raw.product_id.tracking == 'serial':
                            serials_numbers = serials_dict[raw.product_id.name]
                            # Get just the number of serials needed for each
                            # finished product
                            raw_qty = int(
                                raw.product_uom_qty/finished.product_qty)
                            for _qty in range(raw_qty):
                                # Get first serial and remove it after
                                serial = serials_numbers[0]
                                serials_numbers.remove(serial)
                                raw_lot_obj = self.env[
                                    'stock.production.lot'].search([(
                                        'name', '=', serial)])
                                if not raw_lot_obj:
                                    raise ValidationError(_(
                                        'The following lots does not exist'
                                        ' for this material.'
                                        '\n\n Lot: %s' % (serial)))
                                raw.active_move_lot_ids = [(0, 0, {
                                    'lot_id': raw_lot_obj.id,
                                    'quantity_done': 1,
                                    'lot_produced_id': fin_lot_obj.id,
                                    'production_id': mrp_obj.id,
                                })]

    '''
        Function to read the Excel and create the following dicts:

        serials_dict
        key: product name
        value: list of serial numbers to use on the production

        notes_dict
        key: finished product serial
        value: values from notes column
    '''
    @api.multi
    def format_excel_data(self):
        file = tempfile.NamedTemporaryFile(suffix=".xls")
        file.write(binascii.a2b_base64(self.data))
        file.seek(0)
        workbook = xlrd.open_workbook(file.name)
        sheet = workbook.sheet_by_index(0)
        serials_dict = {}
        notes_dict = {}

        for col in range(sheet.ncols):
            product_name = sheet.cell(0, col).value
            serial_numbers = []
            row = 1
            end_col = False

            # Custom functionality to add a note to each finished product
            if product_name in ['notes', 'Notes', 'notas', 'Notas']:
                while not end_col:
                    try:
                        notes_dict.update({
                            sheet.cell(
                                row, 0).value: sheet.cell(row, col).value,
                        })
                        row += 1
                    except IndexError:
                        end_col = True
            else:
                while not end_col:
                    try:
                        if sheet.cell(row, col).value:
                            serial_numbers.append(sheet.cell(row, col).value)
                        row += 1
                    except IndexError:
                        end_col = True

                serials_dict.update({
                    product_name: serial_numbers,
                })

        self.import_serial_numbers(serials_dict, notes_dict)

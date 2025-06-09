# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.

from odoo import models, fields,api

class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'



    def change_vendor(self):
        return {
            'name': ('Change Vendor'),
            'type': 'ir.actions.act_window',
            'res_model': 'change.vendor.wizard',
            'view_mode': 'form',
            'target': 'new',
         }

class AccountMoveLine(models.Model):
    _inherit = 'account.move.line'

    def _check_reconciliation(self):
        for line in self:
            if line.matched_debit_ids or line.matched_credit_ids:
                pass


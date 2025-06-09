# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.


from odoo import models, fields, api



class ChangeVendorWizard(models.TransientModel):
    _name = 'change.vendor.wizard'
    _description = 'Select a new vendor'

    purchase_id = fields.Many2one('res.partner',string="Select Vendor")


    def confirm_button(self):
        partner_id = self.env['purchase.order'].browse(self._context.get('active_id'))
        value = partner_id.update({'partner_id': self.purchase_id.id})
        search_incoming_id = self.env['stock.picking'].search([('origin', '=', partner_id.name)])
        if search_incoming_id:
            for rec in search_incoming_id:
                rec.update({'partner_id': self.purchase_id.id})
        else:
            pass
        bill_id = self.env['account.move'].search([('invoice_origin', '=', partner_id.name)])
        if bill_id:
            for ids in bill_id:
                ids.update({'partner_id': self.purchase_id.id})
                payment_id = self.env['account.payment'].search(['|',('ref', '=', ids.name),('ref', 'ilike', ids.name)])
                if payment_id:
                    for record in payment_id:
                        record.update({'partner_id': self.purchase_id.id})
                        account_id = self.env['account.move'].search([('name', '=', record.name)])
                        for rec in account_id:
                          journal_id = self.env['account.move.line'].search(['|',('move_id.id', '=', rec.id),('move_id.id', '=', ids.id)])
                          reversed_id = self.env['account.move.line'].search([('move_id.name','ilike',ids.name)])
                          for ans in journal_id:
                              ans.update({'partner_id': self.purchase_id.id})
                          for answer in reversed_id:
                              answer.update({'partner_id': self.purchase_id.id})
                              answer.move_id.update({'partner_id': self.purchase_id.id})
                else:
                    journal_id = self.env['account.move.line'].search(['|', ('move_id.name', 'ilike', ids.name), ('move_id.id', '=', ids.id)])
                    if journal_id:
                        for ans in journal_id:
                            ans.update({'partner_id': self.purchase_id.id})
                    else:
                        pass

        else:
            pass

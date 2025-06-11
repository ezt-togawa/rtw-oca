# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.
{
    'name': "Change Vendor In Validated Purchase",
    'version': '14.0.0.0',
    'category': 'Purchases',
    'summary': "Update Supplier in Confirmed Purchase Orders Replace Vendor in Validate Purchase RFQ Change Partner in Purchase Approve Order Vendor Change in Request for Quotation Update Vendor In Validated Purchase Confirm Change Supplier Purchase Replace Vendor in RFQ",
    'description': """
      
        Change Vendor in Validated Purchase Odoo App helps users to change the vendor in validated or confirmed purchase order. Once user can changed vendor in purchase order, It will automatically update in the receipt, bills, journal entry, journal items, payment, and partner ledger.

    """,
    'author': 'BrowseInfo',
    "price": 15,
    "currency": 'EUR',
    'website': 'https://www.browseinfo.com',
    'depends': ['base','sale_management','purchase','account','stock'],
    'data': [
        'security/ir.model.access.csv',
        'security/security.xml',
        'views/account_move_views.xml',
        'views/purchase_order_views.xml',
        'wizard/change_vendor_wizard_views.xml',
    ],
    'license':'OPL-1',
    'installable': True,
    'auto_install': False,
    'live_test_url':'https://youtu.be/v8qKOtyf-Qw',
    "images":['static/description/Change-Vendor-Validated-Purchase-Banner.gif'],
}

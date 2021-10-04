# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'Sale',
    'version': '1.1',
    'author': 'Rashid-Odoo-Master',
    'summary': 'Goods Record',
    'sequence': 10,
    'description': """ this is summary description""",
    'category': 'Extra Tools',
    'website': 'https://www.odoo.com/page/billing',
    'images': ['images/accounts.jpeg', 'images/bank_statement.jpeg', 'images/cash_register.jpeg',
               'images/chart_of_accounts.jpeg', 'images/customer_invoice.jpeg', 'images/journal_entries.jpeg'],
    'depends': ['base_setup', 'product', 'analytic', 'portal', 'digest'],
    'data': [
        'template/record.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}

from odoo import models, fields


class AccountReport(models.Model):
    _name = "account.report"
    _description = "Account Report"

    customer_name = fields.Char(string="Name",require=True)
    customer_age = fields.Integer("Age")
    customer_totalAmount = fields.Char(string="Amount",require=True)
    customer_address = fields.Char(string="Address",require=True)
    customer_picture = fields.Binary(string="Picture")

from odoo import models, fields


class SalesReport(models.Model):
    _name = "sales.report"
    _description = "Customer Sales Report"

    shipment_address = fields.Char(string="Address", require=True)
    total_amount = fields.Integer("Total")
    total_commission = fields.Char(string="Commission", require=True)
    sales_code = fields.Char(string="Code", require=True)
    sales_date = fields.Date(string="Date")
    customer_id = fields.Many2one('customer.data', string="Customer")

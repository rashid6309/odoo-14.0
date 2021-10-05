from odoo import models, fields


class CustomerRecord(models.Model):
    _name = "customer.record"
    _description = "Customer Record"

    customer_name = fields.Char(string="Name", require=True)
    customer_age = fields.Integer("Age")
    customer_address = fields.Char(string="Address", require=True)
    customer_contact = fields.Char(string="Contact", require=True)
    customer_email = fields.Char(string="Email", require=True)
    customer_picture = fields.Binary(string="Picture")


class CustomerRecordRelation(models.Model):
    _name = "customer.record.data"
    _description = "Customer Record Data"
    report_id = fields.Many2one("account.report", string="Report")
    recordId=fields.Many2one("customer.record",string="recordID")

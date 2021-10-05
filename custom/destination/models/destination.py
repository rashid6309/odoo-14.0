from odoo import models, fields


class Destination(models.Model):
    _name = "destination.package"
    _description = "Destination Package Details"

    package_name = fields.Char(string="Name", require=True)
    package_days = fields.Integer("days")
    city = fields.Char(string="City", require=True)
    package_details = fields.Char(string="Details", require=True)
    contact_details = fields.Char(string="Contact", require=True)


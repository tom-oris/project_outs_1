
from odoo import fields, models


class ResCompany(models.Model):
    _inherit = "res.company"

    account_delay_payment_finance_charge = fields.Boolean(string='Delay Payment Finance Charges')

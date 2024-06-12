from odoo import fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    account_delay_payment_finance_charge = fields.Boolean(
        string="Delay Payment Finance Charges", related="company_id.account_delay_payment_finance_charge",
        readonly=False)

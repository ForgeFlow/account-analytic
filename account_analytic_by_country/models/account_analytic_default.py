# Copyright 2021 ForgeFlow S.L. (https://www.forgeflow.com)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl)

from odoo import api, fields, models, _
from odoo.osv import expression


class AccountAnalyticDefault(models.Model):
    _inherit = "account.analytic.default"

    country_id = fields.Many2one(
        'res.country',
        string='Country',
        ondelete='cascade',
        help="Select a country which will use analytic account specified in analytic default "
             "(e.g. create new customer invoice or Sales order if we select a partner of this country, "
             "it will automatically take this as an analytic account)"
    )
    catch_all_countries = fields.Boolean(
        string='Catch all countries analytic account',
        help="Enabling this option the analytic account will be the default catch-all analytic account "
             "for the other countries not defined specifically"
    )

    @api.model
    def account_get(self, product_id=None, partner_id=None, user_id=None, date=None, company_id=None):
        res = super(AccountAnalyticDefault, self).account_get(product_id, partner_id, user_id, date, company_id)
        domain = [('company_id', '=', False)]
        if company_id:
            domain = expression.OR([domain, [("company_id", "=", company_id)]])
        if partner_id:
            partner = self.env['res.partner'].browse(partner_id)
            if partner.country_id:
                res = self.search(expression.AND([domain, [('country_id', '=', partner.country_id.id)]]))
                if not res:
                    res = self.search(expression.AND([domain, [('catch_all_countries', '=', True)]]))
        return res

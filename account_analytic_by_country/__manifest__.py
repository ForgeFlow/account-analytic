# Copyright 2021 ForgeFlow S.L. (https://www.forgeflow.com)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
{
    "name": "Analytic Account By Country",
    "summary": "Allows to define analytic account by country",
    "version": "12.0.1.0.0",
    "development_status": "Beta",
    "category": "Accounting",
    "author": "ForgeFlow, Odoo Community Association (OCA)",
    "license": "AGPL-3",
    "depends": [
        "account_analytic_default",
    ],
    'data': [
        'views/account_analytic_default.xml',
    ],
    "installable": True,
    "auto_install": False,
}

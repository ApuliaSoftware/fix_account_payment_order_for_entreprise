# Copyright 2020 Ilaria Franchini <i.franchini@apuliasoftware.it>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
{
    'name': 'Fix menu account_payment_order OCA for enterprise',
    'version': '12.0.1.0.0',
    'author': 'Apulia software',
    'category': 'Localization/Italy',
    'summary': 'Fix menu account payment order OCA for enterprise',
    'website': 'http://www.apuliasoftware.it',
    'depends' : [
                 'account_payment_order',
                ],
    'data': [
        'views/account_payment_order_view.xml'
            ],
    'installable': True,
}

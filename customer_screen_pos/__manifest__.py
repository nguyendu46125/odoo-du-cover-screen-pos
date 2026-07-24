# -*- coding: utf-8 -*-

{
    'name': "Customer Screen POS",
    'version': '14.0.1.0.0',
    'category': 'Point of Sale',
    'summary': 'This helps customers finalize their order and may add rating '
               'and review.',
    'description': "A separate POS screen for customers to know their ordered "
                   "products and add their review and rating about services",
    'author': 'Du-IT',
    'company': 'Vong Xanh Company',
    'maintainer': 'Du-IT',
    'price': '10.0',
    'currency': 'USD',
    'website': 'https://vdu.vn',
    'depends': ['point_of_sale'],
    'data': [
        'security/ir.model.access.csv',
        'views/assets.xml',
        'views/pos_config_views.xml',
        'views/pos_order_views.xml',
        'views/pos_orderlines_templates.xml',
    ],
    'qweb': [
        'static/src/xml/pos_systray_icon.xml',
    ],
    'images': ['static/description/banner.jpg'],
    'license': 'AGPL-3',
    'installable': True,
    'auto_install': False,
    'application': False,
}

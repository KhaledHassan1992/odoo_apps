# -*- coding: utf-8 -*-
{
    'name': "so_max_quantity_allowed",

    'summary': """sale order product maximum quantity allowed""",

    'description': """allow product maximum quantity in product template 
    and and make warning if ypu exceed maximum quantity""",

    'author': "KhaledHassan",
    'website': 'https://www.linkedin.com/in/khaled-hassan-222600173/',
    'category': 'sale',
    'version': '0.1',
    'depends': ['base', 'product', 'sale'],
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
    ],
    'images': ['static/description/3.jpg','static/description/4.jpg ],
}

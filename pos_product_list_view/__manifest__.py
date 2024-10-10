# -*- coding: utf-8 -*-
{
    'name': 'POS Product List',
    'description': """
        Product Show in list view in Pont of Sale without configuration 
""",
    'version': '12.0',
    'author': "Khaled Hassan",
    'license': 'LGPL-3',
    'price': 3,
    'currency': 'EUR',
    'summary': """show product in list view in point of sale module""",
    'category': 'Point of Sale',
    'depends': ['point_of_sale'],
    'data': [   
                'views/point_of_sale.xml',
             ],
    'images': ['static/description/list_view.jpg'],
    'qweb': ['static/xml/pos.xml'
             ],
}

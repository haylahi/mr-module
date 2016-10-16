# -*- coding: utf-8 -*-
{
    'name': "Product Barcode Generator",

    'summary': """
        This module generates barcode image from the product barcode field.""",

    'description': """
        This module is capable of generating barocde images for the product templates.
        Just provide the barcode number of the product in the barcode field of the product form view.
        It will automatically generate barcode image for the product. And it's Done !!!  

        ##################################################################
        ###     Developers Doc - Please install requirements.txt       ###
        ##################################################################
    """,

    'author': "Mr Module",
    'price': 30.00,
    'currency':'USD',

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Product',
    'version': '0.1',

    'website':'opensys',
    # any module necessary for this one to work correctly
    'depends': ['product', 'sale'],

    # always loaded
    'data': [
        'views/views.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        
    ],
}
{
    'name': 'CustomizeMe',
    'category': 'Website/Website',
    'summary': 'customizeme',
    'author': 'LetzCode',
    'version': '1.0.0',
    'description': """
Boost your sales and customer satisfaction with CustomizeMe for Odoo!
    """,
    'depends': ['website', 'sale', 'website_sale'],
    'data': [
        'views/customizeme_product.xml',
        'views/customizeme_product_frontend.xml',
        'views/customizeme_settings.xml',
    ],
    'application': True,
    'installable': True,
    'auto_install': False,
}

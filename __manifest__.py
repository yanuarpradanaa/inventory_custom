# -*- coding: utf-8 -*-
{
    'name': "Inventory Custom",
    'summary': """
        Beberapa perubahan pada menu Inventory dan sub-subnya""",
    'description': """
     v10.0.2.0 (31-03-2020):\n
     - Inventory\n
      - Product Description otomatis terisi Product Category dan Nama Produk\n
     - Account Invoice\n
      - Description otomatis terisi Product Category dan Nama Product\n
     Maintenance 05-03-2020:\n
     - [FIX-BUG]\n
    Custom:\n
    - [NEW] Autofill Product Description field\n
    - [ADD] UoM field in TreeView 
    """,
    'author': "Satusoft",
    'website': "https://satusoft.com/",
    'category': 'Custom Module',
    'version': '2.0',
    'depends': ['base', 'purchase', 'desc_on_picking'],
    'data': [
        'views/views.xml',
    ],
}
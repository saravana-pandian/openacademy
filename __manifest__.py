# -*- coding: utf-8 -*-
{
    'name': "openacademy",
    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        this open academy module is for odoo technical training
    """,
    'author': "__s_a_r_v_a_n_a___",
    'website': "http://www.yourcompany.com",
    'sequence': "-1000",
    'category': 'Uncategorized',
    'version': '0.1',
    'depends': ['base', 'hr', 'website_slides'],
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'wizard/regist.xml',
        'views/views.xml',
        'views/templates.xml',
        'views/openacademy.xml',
        'views/session.xml',
        'views/partner.xml'
        
    ],
    'demo': [
        'demo/demo.xml',
    ],
}

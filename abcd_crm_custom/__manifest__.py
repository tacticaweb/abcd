# -*- coding: utf-8 -*-
{
    'name': 'ABC&D - Personalizaciones CRM',
    'description': "Personalización modulo CRM para empresa ABC&D",
    'author': "SOLUCIONES OPEN SOURCE",
    'website': "http://www.solucionesos.com",
    'summary': "ABC&D - CRM Custom",
    'version': '0.1',
    "license": "OPL-1",
    'support': 'luis.m.varon@gmail.com',
    'category': 'module_crm',
        # any module necessary for this one to work correctly
    'depends': ['crm','sales_team'],

    # always loaded
    'data': [
             'views/views.xml',
            ],
    'qweb': [
               
            ],
    #"external_dependencies": {"python" : ["pytesseract"]},
    'installable': True,
}

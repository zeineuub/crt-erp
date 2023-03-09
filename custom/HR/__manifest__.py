{
    'name': 'Humain Resource Management',
    'description': "Volunteers management in red crescent",
    'version': '1.0',
    'author': "Malek & Ghada",
    'depends': ['base'],
    'category': 'Humain Resources',
    'data': [
        'views/hr.xml',
        'security/ir.model.access.csv'

    ],
    'summary': 'this module add, update and delete volunteers',
    'license': 'LGPL-3',
    'application': True,
    'installable': True,
    'auto_install': False,
    'sequence':2,
}

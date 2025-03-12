{
    'name': 'Hospital Management',
    'sequence' : 1,
    'version': '1.0',
    'summary': 'A module for managing hospital operations',
    'description': 'This module helps manage hospital patients, doctors, appointments, and other medical activities.',
    'author': 'Rakib Hasan',
    'website': 'https://yourwebsite.com',
    'category': 'Healthcare',
    'depends': ['mail'],
    'data': [
        # Add your XML, CSV, or security files here
        'security/ir.model.access.csv',

        'views/patient_view.xml',
        'views/patient_view_readonly.xml',
        'views/menu.xml',
    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}

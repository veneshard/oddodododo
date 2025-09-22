{
    'name': 'Training Kendaraan',
    'summary': 'Modul manajemen kendaraan, kontrak, biaya, dan servis seperti Fleet Odoo',
    'description': '''
Modul Training Kendaraan untuk manajemen armada, kontrak, biaya, servis, dan pelacakan kendaraan.
Fitur mirip Fleet Odoo, lengkap dengan menu, hak akses, dan dashboard analisis.
''',
    'author': 'Your Company',
    'website': 'https://yourcompany.com',
    'category': 'Fleet',
    'version': '1.0',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/vehicle_fuel_views.xml',
    ],
    'images': ['static/description/icon.png'],
    'installable': True,
    'application': True,
}

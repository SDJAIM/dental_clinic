{
    'name': 'Dental Clinic Management System',
    'version': '1.0',
    'sequence': -101,
    'category': 'Industries/Healthcare',
    'summary': 'Management',
    'description': """Helping you to ensure a great experience""",
    'depends': [
        'base', 'account', 'calendar', 'sales_team', 'payment', 'portal', 'utm',
        'sale', 'mail', 'crm', 'point_of_sale', 'base_setup', 'web', 'product'
    ],
    'data': [
        # 'security/security.xml',
        'security/ir.model.access.csv',
        'data/data.xml',
        # 'wizard/remove_invoice_views.xml',
        'views/appointment_view.xml',
        'views/patient_view.xml',
        # 'views/backend.xml',
        'views/Patient_Appointment_Form_view_customization.xml',
        'views/inventory_stock.xml',
        'report/report_sale_receipt_template.xml',
        # 'report/report.xml',
    ],
    'qweb': [
        'static/src/xml/toothChart.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}

{
    'name': 'ProConsult Invoice',
    'version': '18.0.1.0',   
    'category': 'Accounting',
    'summary': 'Gestion commerciale',
    'author': 'Jonah Harivelona',
    'depends': ['account', 'proconsult_sale'], 
    'data': [
        'report/invoice_report.xml',
        'report/invoice_report_template.xml',
        'views/account_move_views.xml'
    ],
    'installable' :True,
    'licence':'LGPL-3' 
}
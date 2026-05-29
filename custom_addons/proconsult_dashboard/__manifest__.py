{
    'name': 'ProConsult Dashboard',
    'version': '18.0.1.0',   
    'category': 'Sales',
    'summary': 'Gestion commerciale',
    'author': 'Jonah Harivelona',
    'depends': ['sale', 'proconsult_sale'], 
    'data': [
        'security/ir.model.access.csv',
        'views/sale_report_view.xml',
    ],
    'installable' :True,
    'licence':'LGPL-3' 
}
{
    'name': 'ProConsult Relance',
    'version': '18.0.1.0',   
    'category': 'accounting',
    'summary': 'Gestion commerciale',
    'author': 'Jonah Harivelona',
    'depends': ['account', 'mail', 'proconsult_invoice'], 
    'data': [
        'security/ir.model.access.csv',
        'data/mail_template.xml',
        'views/relance_wizard_views.xml'
    ],
    'installable' :True,
    'licence':'LGPL-3' 
}
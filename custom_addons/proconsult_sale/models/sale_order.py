from odoo import fields, models

class SaleOrder(models.Model):
    _inherit = 'sale.order'
    
    x_type_prestation = fields.Selection([
        ('Formation', 'formation'),
        ('Consulting', 'consulting'),
        ('Mixte', 'mixte')
    ], default='Formation', string='Type de prestation')
    x_date_debut_prestation = fields.Date(string='Debut prestation')
    x_date_fin_prestation  = fields.Date(string='Fin prestation')
    x_contrat_cadre = fields.Boolean(string='Contrat', default=True)
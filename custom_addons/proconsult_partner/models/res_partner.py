from odoo import models, fields

class ResPartner(models.Model):
    _inherit = 'res.partner'
    
    x_categorie_client = fields.Selection([
    ('pme', 'PME'),
    ('esn', 'ESN'),
    ('administration', 'ADMINISTRATION'),
    ('Particulier', 'PARTICULIER'),
    ], default= 'PME', string='Categorie client')
    x_secteur_activite = fields.Char(string="Secteur d' activite")
    x_commercial_referent = fields.Many2one('res.users', string='Commercial')
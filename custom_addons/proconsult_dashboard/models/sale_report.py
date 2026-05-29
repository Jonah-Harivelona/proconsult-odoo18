from odoo import models, fields

class SaleReport(models.Model):
    _name = 'proconsult.sale.report'
    _description = 'Rapport commercial ProConsult'
    _auto = False
    _rec_name = 'date_order'

    date_order = fields.Date(string='Date')
    partner_id = fields.Many2one('res.partner', string='Client')
    user_id = fields.Many2one('res.users', string='Commercial')
    x_type_prestation = fields.Selection([
        ('formation', 'Formation'),
        ('consulting', 'Consulting'),
        ('mixte', 'Mixte')
    ], string='Type de prestation')
    amount_total = fields.Float(string='Montant total')
    state = fields.Selection([
        ('draft', 'Devis'),
        ('sale', 'Commande'),
        ('done', 'Facturé'),
    ], string='Statut')

    def init(self):
        self.env.cr.execute("""
            CREATE OR REPLACE VIEW proconsult_sale_report AS (
                SELECT
                    so.id,
                    so.date_order::date as date_order,
                    so.partner_id,
                    so.user_id,
                    so.x_type_prestation,
                    so.amount_total,
                    so.state
                FROM sale_order so
                WHERE so.state IN ('sale', 'done')
            )
        """)
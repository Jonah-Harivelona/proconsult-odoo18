from odoo import models, fields

class AccountMove(models.Model):
    _inherit = 'account.move'
    
    x_type_prestation = fields.Selection(
        related='invoice_line_ids.sale_line_ids.order_id.x_type_prestation',
        string='Type de prestation',
        store=True
    )
    x_date_debut_prestation = fields.Date(
        related='invoice_line_ids.sale_line_ids.order_id.x_date_debut_prestation',
        string='Date début prestation',
        tore=True
    )

    x_date_fin_prestation = fields.Date(
        related='invoice_line_ids.sale_line_ids.order_id.x_date_fin_prestation',
        string='Date fin prestation',
        store=True
    )
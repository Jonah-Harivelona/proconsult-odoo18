from odoo import models, fields, _
from odoo.exceptions import UserError

class RelanceWizard(models.TransientModel):
    _name = 'proconsult.relance'
    _description = 'Relance commerciale personnalise'
    
    date_limite = fields.Date(string='Date limite de paiement depassée')
    partner_ids = fields.Many2many('res.partner', string='Client')
    message_personnalise = fields.Text(string='Message a envoye')
    
    def action_envoyer_relance(self):
        
        self.ensure_one() 
        if not self.partner_ids:
            raise UserError(_("Veuillez sélectionner au moins un client avant d'envoyer la relance."))

        template = self.env.ref('proconsult_relance.email_template_relance_proconsult', raise_if_not_found=False)
        
        if not template:
            raise UserError(_("Le modèle d'email requis n'a pas pu être trouvé."))

        compteur_envois = 0
        for partner in self.partner_ids:
            if partner.email:
                template.with_context(lang=partner.lang).send_mail(
                    partner.id, 
                    force_send=True, 
                    email_values={'email_to': partner.email} 
                )
                compteur_envois += 1
            else:
                pass

        return {
            'type': 'ir.actions.client',
            'tag': 'display_notification',
            'params': {
                'title': _('Relance envoyée'),
                'message': _('%s email(s) de relance ont été envoyés avec succès.', compteur_envois),
                'sticky': False,
                'type': 'success',
                }
      }
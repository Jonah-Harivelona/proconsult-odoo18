Cahier des charges technique
ProConsult Tana — Système de gestion commerciale sur Odoo 18

1. Présentation du contexte

    Entreprise : ProConsult Tana
    Secteur : Formation professionnelle et consulting IT
    Localisation : Antananarivo, Madagascar
    Taille : PME de 15 personnes dont 3 commerciaux
    Activité : ProConsult Tana propose des formations informatiques certifiantes et des missions de conseil en transformation digitale pour les PME et ESN malgaches.

2. Problématique
Aujourd'hui ProConsult Tana gère tout manuellement :

    Les prospects sont suivis sur Excel
    Les devis sont faits sur Word, envoyés par email
    Les contrats de formation sont signés en papier
    Les factures sont créées manuellement, les relances oubliées
    Aucun responsable n'a de vision globale sur le chiffre d'affaires

Objectif : Centraliser toute la gestion commerciale sur Odoo 18 avec des développements spécifiques adaptés au métier de ProConsult Tana.

3. Périmètre fonctionnel

    Gérer les prospects et clients avec des informations métier spécifiques
    Créer et envoyer des devis de formation ou de consulting
    Transformer un devis en bon de commande puis en facture
    Gérer les contrats de formation avec dates et renouvellement
    Envoyer des relances automatiques aux clients en retard de paiement
    Visualiser le chiffre d'affaires par commercial et par type de service

4. Périmètre technique
Modules Odoo natifs utilisés

    Module natif        Rôle
    
    res.partner         Base clients et prospects
    sale.order          Devis et commandes
    account.move        Factures
    crm.lead            Pipeline commercial
    mail.thread         Messagerie et relances

Modules custom à créer

    Module custom           Rôle
    proconsult_partner      Extension du modèle client
    proconsult_sale         Personnalisation des devis et commandes
    proconsult_invoice      Rapport de facture personnalisé QWeb
    proconsult_relance      Wizard de relance client

5. Modèle de données

res.partner (étendu)
├── x_categorie_client : selection (PME, ESN, Administration, Particulier)
├── x_secteur_activite : char
└── x_commercial_referent : many2one → res.users

sale.order (étendu)
├── x_type_prestation : selection (Formation, Consulting, Mixte)
├── x_date_debut_prestation : date
├── x_date_fin_prestation : date
└── x_contrat_cadre : boolean

account.move (étendu)
└── x_type_prestation : related → sale.order.x_type_prestation

proconsult.relance (TransientModel)
├── date_limite : date
├── partner_ids : many2many → res.partner
└── message_personnalise : text
# Architecture technique — ProConsult Tana

## Dépendances entre modules

proconsult_partner
└── proconsult_sale
├── proconsult_invoice
│   └── proconsult_relance
└── proconsult_dashboard

## Modèles étendus

| Modèle natif | Module | Champs ajoutés |
|---|---|---|
| res.partner | proconsult_partner | x_categorie_client, x_secteur_activite, x_commercial_referent |
| sale.order | proconsult_sale | x_type_prestation, x_date_debut_prestation, x_date_fin_prestation, x_contrat_cadre |
| account.move | proconsult_invoice | x_type_prestation, x_date_debut_prestation, x_date_fin_prestation |

## Modèles créés

| Modèle | Module | Type | Description |
|---|---|---|---|
| proconsult.relance | proconsult_relance | TransientModel | Wizard de relance client |
| proconsult.sale.report | proconsult_dashboard | Vue SQL (_auto=False) | Reporting commercial |

## Vues créées

| Vue | Modèle | Type |
|---|---|---|
| Onglet ProConsult | res.partner | Héritage formulaire |
| Onglet ProConsult | sale.order | Héritage formulaire |
| Champ type prestation | account.move | Héritage formulaire |
| Wizard relance | proconsult.relance | Formulaire popup |
| Tableau de bord liste | proconsult.sale.report | Liste |
| Tableau de bord pivot | proconsult.sale.report | Pivot |
| Tableau de bord graph | proconsult.sale.report | Graph |

## Rapport créé

| Rapport | Modèle | Format |
|---|---|---|
| Facture ProConsult Tana | account.move | PDF QWeb |

## Stack technique

- Odoo 18 Community
- Python 3.10
- PostgreSQL 14
- XML / QWeb
- Git / GitHub
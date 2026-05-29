# ProConsult Tana — Système de gestion commerciale Odoo 18

## Contexte
ProConsult Tana est une PME fictive basée à Antananarivo, Madagascar, 
spécialisée dans la formation professionnelle et le consulting IT. 
Ce projet simule le déploiement d'un système de gestion commerciale 
complet sur Odoo 18, réalisé dans le cadre d'un projet personnel 
de montée en compétences sur le développement Odoo.

## Modules développés

| Module | Description |
|---|---|
| `proconsult_partner` | Extension du modèle client avec champs métier spécifiques |
| `proconsult_sale` | Personnalisation des devis et commandes |
| `proconsult_invoice` | Rapport de facture PDF personnalisé QWeb |
| `proconsult_relance` | Wizard de relance client par email |
| `proconsult_dashboard` | Tableau de bord commercial avec vues pivot et graph |

## Prérequis

- Odoo 18 Community
- PostgreSQL 14+
- Python 3.10+

## Installation

1. Cloner le dépôt :
git clone https://github.com/Jonah-Harivelona/proconsult-odoo18.git

2. Copier les modules dans ton dossier addons :
cp -r custom_addons/* /chemin/vers/odoo/custom_addons/

3. Ajouter le chemin dans odoo.conf :
addons_path = /chemin/vers/odoo/custom_addons

4. Installer les modules dans cet ordre depuis Odoo :
- proconsult_partner
- proconsult_sale
- proconsult_invoice
- proconsult_relance
- proconsult_dashboard

## Structure du projet

proconsult-odoo18/
├── custom_addons/
│   ├── proconsult_partner/
│   ├── proconsult_sale/
│   ├── proconsult_invoice/
│   ├── proconsult_relance/
│   └── proconsult_dashboard/
├── docs/
│   ├── cahier_des_charges.md
│   └── architecture.md
├── .gitignore
└── README.md

## Auteur
Jonah Harivelona
Étudiant M1 Informatique — Madagascar
2026
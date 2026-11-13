# Gestion de stock

Application web de gestion de stock réalisée avec Django dans le cadre du TP collaboratif GitHub et déploiement Django.

## Fonctionnalités

- Créer, consulter, modifier et supprimer des produits.
- Associer chaque produit à une catégorie et filtrer la liste par catégorie.
- Afficher les produits dont la quantité est inférieure au seuil d’alerte.
- Administrer les catégories et produits depuis Django Admin.

## Modèles

- **Categorie** : nom et description facultative.
- **Produit** : nom, quantité, seuil d’alerte, catégorie et dates d’ajout/modification.

Une quantité égale au seuil ne déclenche pas d’alerte ; l’alerte s’applique si `quantite < seuil_alerte`.

## Prérequis

Python 3, pip et Git. Les dépendances Python sont listées dans `requirements.txt`.

## Installation locale

```bash
git clone https://github.com/Lordex-hasg/TP_Groupe_GitHub_Deploiement_Django.git
cd TP_Groupe_GitHub_Deploiement_Django
python -m venv venv
```

Activer l’environnement virtuel :

**Windows PowerShell**
```powershell
.\venv\Scripts\Activate.ps1
```

**macOS / Linux**
```bash
source venv/bin/activate
```

Installer les dépendances et initialiser la base :

```bash
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Ouvrir http://127.0.0.1:8000/stock/ pour la gestion du stock ou http://127.0.0.1:8000/admin/ pour l’administration.

## Tests

Lancer les tests Django avec :

```bash
python manage.py test
```

Parcours à vérifier : création, liste, filtre par catégorie, modification, suppression et alerte de stock.

## Déploiement

En production, fournir `SECRET_KEY` par variable d’environnement, désactiver le mode debug, configurer `ALLOWED_HOSTS`, les fichiers statiques et la base de données selon l’hébergeur.

## Dépôt

https://github.com/Lordex-hasg/TP_Groupe_GitHub_Deploiement_Django

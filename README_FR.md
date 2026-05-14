# CSV JSON Data Analyzer

Un projet d’apprentissage Python consacré à la lecture, au nettoyage, à l’analyse et à l’export de données structurées avec des fichiers CSV et JSON.

Ce dépôt fait partie de ma roadmap personnelle de progression développeur. L’objectif est de renforcer mes bases sur la manipulation de fichiers, les données structurées, le nettoyage de données et la génération de rapports avec Python et la bibliothèque standard.

Ce projet est indépendant de tout projet produit ou business.

---

## Objectifs

Les objectifs principaux de ce dépôt sont de :

- Comprendre la différence entre un dictionnaire Python et du JSON
- Lire des fichiers JSON
- Écrire des fichiers JSON
- Convertir une chaîne JSON en objets Python
- Convertir des objets Python en chaîne JSON
- Lire des fichiers CSV
- Utiliser `csv.DictReader`
- Utiliser `csv.DictWriter`
- Nettoyer et convertir des données brutes
- Gérer proprement les erreurs de fichier et de données
- Exporter des rapports simples en JSON, CSV ou texte

---

## Sujets couverts

| Bloc | Sujet | Statut |
| --- | --- | --- |
| 15.1 | Différence entre dict Python et JSON | Validé |
| 15.2 | Lire JSON avec `json.load()` | Validé |
| 15.3 | Écrire JSON avec `json.dump()` | Validé |
| 15.4 | Convertir une string JSON avec `json.loads()` | Validé |
| 15.5 | Convertir dict/list avec `json.dumps()` | Validé |
| 15.6 | Lire un CSV simple | Validé |
| 15.7 | Lire un CSV avec `csv.DictReader` | Validé |
| 15.8 | Écrire un CSV avec `csv.DictWriter` | Validé |
| 15.9 | Nettoyer et convertir des données CSV | Validé |
| 15.10 | Gérer les erreurs de fichier et de données | À faire |
| 15.11 | Mini-consolidation CSV/JSON | À faire |
| 15.12 | Projet final CSV/JSON analyzer | À faire |

---

## Structure du projet

```text
csv-json-data-analyzer/
├── data/
│   ├── input/
│   │   └── products.csv
│   └── output/
│       └── .gitkeep
├── exercises/
│   ├── block_15_1_dict_vs_json.py
│   ├── block_15_json_basics.py
│   └── block_15_csv_basics.py
├── README.md
├── README_FR.md
└── .gitignore
```

> Note : ce dépôt reste volontairement simple. Les exercices sont exécutés fichier par fichier. Un `main.py` central n’est pas nécessaire à ce stade.

> Les fichiers générés dans `data/output/` sont ignorés par Git.

---

## Exécution

Chaque exercice peut être lancé indépendamment depuis la racine du projet.

Exemples :

```bash
python exercises/block_15_1_dict_vs_json.py
python exercises/block_15_json_basics.py
python exercises/block_15_csv_basics.py
```

L’exercice CSV basics lit les données depuis :

```text
data/input/products.csv
```

et exporte un fichier CSV nettoyé vers :

```text
data/output/clean_products.csv
```

Les fichiers générés dans `data/output/` sont ignorés par Git.

---

## Exercices validés

### 15.1 — Dict Python vs JSON

Cet exercice introduit la différence entre :

- les dictionnaires Python
- les chaînes JSON
- les booléens Python : `True`, `False`
- les booléens JSON : `true`, `false`
- la valeur Python `None`
- la valeur JSON `null`

Il introduit aussi :

```python
json.dumps()
json.loads()
```

---

### 15.2 à 15.5 — Bases JSON

Cet exercice pratique les quatre fonctions principales de conversion JSON :

```python
json.dumps()  # Python -> string JSON
json.loads()  # string JSON -> Python
json.dump()   # Python -> fichier JSON
json.load()   # fichier JSON -> Python
```

Il permet aussi de pratiquer :

- l’écriture de fichiers JSON
- la lecture de fichiers JSON
- l’utilisation de `encoding="utf-8"`
- l’utilisation de `indent=4`
- l’utilisation de `ensure_ascii=False`
- la conservation des accents dans les fichiers JSON

---

### 15.6 à 15.9 — Bases CSV

Cet exercice permet de pratiquer la lecture, le nettoyage, l’analyse et l’export de données CSV.

Il couvre :

- la lecture de fichiers CSV avec `csv.DictReader`
- l’écriture de fichiers CSV avec `csv.DictWriter`
- l’utilisation de `newline=""`
- le nettoyage des textes avec `.strip()`
- la normalisation des textes avec `.lower()`
- la conversion des valeurs avec `int()` et `float()`
- le comptage de produits par catégorie
- le calcul de la valeur totale du stock
- l’export de données CSV nettoyées

---

## Objectif du projet final

Le projet final analysera des données structurées provenant de fichiers CSV et JSON.

Il devra être capable de :

- Lire des données brutes
- Nettoyer les champs texte
- Convertir les valeurs numériques
- Détecter les lignes invalides
- Compter les éléments par catégorie ou statut
- Calculer des totaux simples
- Exporter un rapport propre

Exemple de sortie finale :

```python
{
    "total_records": 120,
    "valid_records": 113,
    "invalid_records": 7,
    "categories": {
        "food": 45,
        "tools": 30,
        "other": 38
    }
}
```

---

## Ce que je pratique

À travers ce dépôt, je pratique :

- la manipulation de données structurées
- la lecture et l’écriture de fichiers
- la transformation de chaînes brutes en valeurs Python propres
- la conversion JSON entre strings, fichiers et objets Python
- la lecture et l’export de fichiers CSV
- la réutilisation de patterns algorithmiques : compteur, accumulateur, filtrage, groupement
- la gestion des cas limites et des données invalides
- la construction de petits scripts réalistes de traitement de données

---

## Cas limites à prévoir

Les exercices et le projet devront gérer :

- les fichiers absents
- les fichiers vides
- les listes vides
- le contenu JSON invalide
- les colonnes CSV manquantes
- les lignes CSV vides
- les valeurs numériques invalides
- les catégories ou statuts inconnus
- les dossiers de sortie qui n’existent pas encore

---

## Améliorations futures

Améliorations possibles :

- Ajouter des tests unitaires avec `pytest`
- Ajouter un vrai point d’entrée CLI
- Refactoriser le projet en modules après le bloc Modules Python
- Ajouter des type hints après le bloc typage
- Ajouter un jeu de données plus grand
- Ajouter une version Pandas plus tard dans le parcours Data

---

## Stack technique

- Python 3
- Bibliothèque standard uniquement :
  - `json`
  - `csv`
  - `pathlib`

Aucune dépendance externe n’est nécessaire à ce stade.

---

## Statut du dépôt

En cours dans le cadre de mon apprentissage Python CSV/JSON et données structurées.

Progression actuelle :

```text
Bases JSON : validées
Bases CSV : validées
Gestion des erreurs fichier/données : prochaine étape
Projet final CSV/JSON analyzer : à venir
```
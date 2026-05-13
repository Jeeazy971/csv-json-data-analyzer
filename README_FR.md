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
| 15.1 | Différence entre dict Python et JSON | À faire |
| 15.2 | Lire JSON avec `json.load()` | À faire |
| 15.3 | Écrire JSON avec `json.dump()` | À faire |
| 15.4 | Convertir une string JSON avec `json.loads()` | À faire |
| 15.5 | Convertir dict/list avec `json.dumps()` | À faire |
| 15.6 | Lire un CSV simple | À faire |
| 15.7 | Lire un CSV avec `csv.DictReader` | À faire |
| 15.8 | Écrire un CSV avec `csv.DictWriter` | À faire |
| 15.9 | Nettoyer et convertir des données CSV | À faire |
| 15.10 | Gérer les erreurs de fichier et de données | À faire |
| 15.11 | Mini-consolidation CSV/JSON | À faire |
| 15.12 | Projet final CSV/JSON analyzer | À faire |

---

## Structure du projet

```text
csv-json-data-analyzer/
├── data/
│   ├── input/
│   └── output/
├── exercises/
├── README.md
├── README_FR.md
└── .gitignore
```

> Note : ce dépôt reste volontairement simple. Les exercices sont exécutés fichier par fichier. Un `main.py` central n’est pas nécessaire à ce stade.

---

## Exécution

Chaque exercice peut être lancé indépendamment.

Exemple :

```bash
python exercises/block_15_1_dict_vs_json.py
```

Plus tard, le script final pourra être lancé avec :

```bash
python exercises/csv_json_data_analyzer.py
```

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

## Ce que je vais pratiquer

À travers ce dépôt, je vais pratiquer :

- La manipulation de données structurées
- La lecture et l’écriture de fichiers
- La transformation de chaînes brutes en valeurs Python propres
- La réutilisation de patterns algorithmiques : compteur, accumulateur, filtrage, groupement
- La gestion des cas limites et des données invalides
- La construction de petits scripts réalistes de traitement de données

---

## Cas limites à prévoir

Les exercices et le projet devront gérer :

- Les fichiers absents
- Les fichiers vides
- Les listes vides
- Le contenu JSON invalide
- Les colonnes CSV manquantes
- Les lignes CSV vides
- Les valeurs numériques invalides
- Les catégories ou statuts inconnus
- Les dossiers de sortie qui n’existent pas encore

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
# Problème — Exercice Python 1.3 : Variables & Structures de données

## Objectif
Créer un programme Python qui collecte des informations utilisateur, les stocke dans des **variables** et les organise avec des **structures de données** :
- `list` (liste)
- `set` (ensemble, pour compter les valeurs uniques)
- `dict` (dictionnaire)
- `tuple` (tuple)

## Consignes
Ton programme doit :

1. Demander à l’utilisateur :
   - **Nom complet** (string)
   - **Ville** (string)
   - **Année de naissance** (int)
   - **Année courante** (int)
   - **Aliments préférés** (une ligne séparée par des virgules)

2. Construire :
   - `age` = `current_year - birth_year`
   - `foods_list` : découpe par `,` puis `strip()` sur chaque élément
   - `foods_set` : `set(foods_list)`
   - `profile_dict` : dictionnaire avec clés (dans cet ordre) : `"name"`, `"city"`, `"age"`, `"foods"`
   - `summary_tuple` : tuple `(name, age, city)`

3. Afficher exactement ces lignes (mêmes libellés) :
```
--------------------
Name: <name>
City: <city>
Age: <age>
Foods (list): <foods_list>
Foods count: <len(foods_list)>
Unique foods: <len(foods_set)>
Profile (dict): <profile_dict>
Summary (tuple): <summary_tuple>
--------------------
```

## Exemple d’interaction
Entrées :
- John Doe
- Kinshasa
- 2000
- 2026
- pizza, burger, pizza

Sortie (exemple) :
```
Enter full name: John Doe
Enter city: Kinshasa
Enter birth year: 2000
Enter current year: 2026
Enter favorite foods (comma-separated): pizza, burger, pizza
--------------------
Name: John Doe
City: Kinshasa
Age: 26
Foods (list): ['pizza', 'burger', 'pizza']
Foods count: 3
Unique foods: 2
Profile (dict): {'name': 'John Doe', 'city': 'Kinshasa', 'age': 26, 'foods': ['pizza', 'burger', 'pizza']}
Summary (tuple): ('John Doe', 26, 'Kinshasa')
--------------------
```

## Tester localement
```bash
pip install -r requirements.txt
pytest -q
```

## Exécuter le programme
```bash
python data_structures.py
```

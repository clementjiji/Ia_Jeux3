# LU3IN025 — IA et Jeux

TME du cours **LU3IN025** à Sorbonne Université. On s'attaque au problème d'affectation des étudiants aux parcours du master Info, avec deux angles : Gale-Shapley d'un côté, PLNE de l'autre.

## De quoi ça parle

Le master Info de la fac propose 10 parcours : AI2D, BIM, CCA, IMA, MIND, QI, RES, SAR, SESI et STL. Chaque année, il faut caser les étudiants quelque part en tenant compte de leurs vœux et du classement des dossiers côté parcours. C'est un problème de mariage stable version "hôpitaux" — un parcours peut accueillir plusieurs étudiants, un étudiant n'en a qu'un.

Le but du TME, c'est de coder ça, de regarder comment ça scale, et de voir ce qu'on peut gagner en passant par de la programmation linéaire.

## Les fichiers de données

- **`PrefEtu.txt`** : ce que les 13 étudiants pensent des 10 parcours.
  - Première ligne : le nombre d'étudiants.
  - Le reste : une ligne par étudiant, avec son classement des parcours.
- **`PrefSpe.txt`** : ce que les parcours pensent des étudiants.
  - Première ligne : le nombre d'étudiants.
  - Deuxième ligne : la capacité de chaque parcours.
  - Le reste : le classement de chaque parcours.

## Ce qu'il y a dans le repo

| Fichier | À quoi ça sert |
|---|---|
| `projet.py` | Le code du projet : lecteurs de fichiers, GS étudiants/parcours, vérif de stabilité, modèles PLNE. |
| `main.py` | Le script qui lance tout sur les fichiers fournis. |
| `exemple.py` | Le bout de code donné avec l'énoncé. |
| `PrefEtu.txt` / `PrefSpe.txt` | Les données de test. |
| `TME.pdf` | L'énoncé. |

## Les questions, dans l'ordre

### Partie 1 — Gale-Shapley

- **Q1** — Lire `PrefEtu.txt` et `PrefSpe.txt`, sortir les matrices Cₑ et Cₚ.
- **Q2** — Réfléchir aux structures de données pour que les opérations de base (étudiant libre, prochain parcours à demander, position dans un classement, étudiant le moins bien classé déjà pris, remplacement) restent rapides.
- **Q3** — GS côté étudiants. Analyse de complexité.
- **Q4** — GS côté parcours.
- **Q5** — On lance les deux sur les fichiers de test.
- **Q6** — Recherche des paires instables pour vérifier que les affectations sont effectivement stables.

### Partie 2 — Quand n grossit

- **Q7** — Tirage aléatoire de Cₑ et Cₚ pour un n donné.
- **Q8** — Temps moyen pour n = 200, 400, …, 2000, au moins 10 tirages par taille, capacités qui somment à n.
- **Q9** — On compare la courbe empirique à la complexité théorique.
- **Q10** — Pareil, mais avec le nombre d'itérations.

### Partie 3 — Équité avec la PLNE

L'utilité d'un étudiant pour un parcours est le score de Borda associé.

- **Q11** — PLNE qui maximise le **min** des utilités (équité maximin).
- **Q12** — PLNE qui maximise la **somme** des utilités (côté étudiants + côté parcours), résolue avec Gurobi. On regarde l'utilité moyenne et l'utilité minimale obtenues.
- **Q13** — Même chose, mais en imposant que chaque étudiant tombe dans son top k (utilité ≥ m − k).
- **Q14** — On cherche le plus petit k pour lequel un mariage parfait existe encore.
- **Q15** — Bilan : on met côte à côte GS étudiants, GS parcours, Q11, Q12 et Q14, et on les compare sur la stabilité, l'utilité moyenne, l'utilité min, et le nombre de paires instables.

## Pour lancer

```bash
python main.py
```

⚠️ Q11–Q14 utilisent **Gurobi** via son binding Python — il faut donc une licence et le solveur installé (la licence académique fait le job).

> Note : dans `main.py`, le chemin vers `PrefEtu.txt` / `PrefSpe.txt` est en absolu. À adapter si vous clonez ailleurs que sur ma machine.

## Auteurs

TME fait en binôme pour l'UE **LU3IN025 — Intelligence Artificielle et Jeux**, Sorbonne Université.

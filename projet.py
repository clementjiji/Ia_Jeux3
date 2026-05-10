import random
import time
import matplotlib.pyplot as plt

#Q1

def prefetu(file):
    f=open(file,'r')
    tab = []
    lignes = f.readline().strip()
    lignes = f.readline().strip()
    while(lignes != ""):
        temp = []
        liste_texte = lignes.split()
        for i in range(2,len(liste_texte)):
            temp.append(int(liste_texte[i]))
        tab.append(temp)
        lignes = f.readline().strip()

    f.close()
    return tab

def prefpar(file):
    f=open(file,'r')
    tab = []
    cap = []
    lignes = f.readline().strip()
    lignes = f.readline().strip()

    cap_ligne = lignes.split()
    for i in range(1,len(cap_ligne)):
        cap.append(int(cap_ligne[i]))

    lignes = f.readline().strip()
    while(lignes != ""):
        temp = []
        liste_texte = lignes.split()
        for i in range(2,len(liste_texte)):
            temp.append(int(liste_texte[i]))
        tab.append(temp)
        lignes = f.readline().strip()

    f.close()
    return cap, tab

#Q2

#1) faire une Pile contenant les etudiant libre O(1)
#2) faire une liste de taille nombre d'etudiant ou l'index i référence l'étudiant i qui contient le numéro du parcour de l'etudiant pour l'iteration O(1)
#3) dans une fonction inverser la matrice prefpar[numParcours][numPreférence] = numEtudiant => inverse[numParcour][numEtudiant] = numPréférence O(1)
#4) dans la fonction inverser en profiter pour remplire une liste type plusNull[numParcour] = numEtudiant O(1)
#5) utilisation d'un dictionnaire qui contient en clé le numéro du parocurs et en valeurs une lite des étudiants qui y sont affectés Dict[numParcours] = [numEtudiant]

#Q3

def inverser(mat):
    resu = []
    pires = []
    
    for i in range(len(mat)):
        temp = [0] * len(mat[0])
        for j in range(len(mat[i])):
            temp[mat[i][j]] = j
        resu.append(temp)
        pires.append(mat[i][len(mat[0])-1])
    return resu,pires


def gs_Etu(tabEtu,tabPar,cap):
    ite = 0
    etuLibre = [n for n in range(len(tabEtu))]
    parSuivEtu = [0] * len(tabEtu)
    inverse_tabPar,pires = inverser(tabPar)
    affectation = {}
    for j in range(len(tabPar)):
        affectation[j] = []
    pires = {}

    while len(etuLibre) > 0:
        ite += 1
        e = etuLibre.pop()
        p = tabEtu[e][parSuivEtu[e]]
        parSuivEtu[e] += 1

        if len(affectation[p]) < cap[p]:
            affectation[p].append(e)
            if p not in pires:
                pires[p] = e
            elif inverse_tabPar[p][e] > inverse_tabPar[p][pires[p]]:
                pires[p] = e

        else:
            if inverse_tabPar[p][e] < inverse_tabPar[p][pires[p]]:
                etuLibre.append(pires[p])
                affectation[p].remove(pires[p])
                affectation[p].append(e)
                pires[p] = affectation[p][0]
                for etu in affectation[p]:
                    if inverse_tabPar[p][etu] > inverse_tabPar[p][pires[p]]:
                        pires[p] = etu
            else:
                etuLibre.append(e)

    return affectation,ite

#Q4

def gs_Par(tabEtu,tabPar,cap):
    ite = 0
    n = len(tabEtu)    
    m = len(tabPar)    
    inverse_tabEtu,_ = inverser(tabEtu)
    etuSuivPar = [0] * m
    affectation = {}
    for j in range(m):
        affectation[j] = []
    affectEtu = [None] * n 

    parLibre = []
    for j in range(m):
        if cap[j] > 0:
            parLibre.append(j)

    while len(parLibre) > 0:
        ite += 1
        p = parLibre.pop()
        if etuSuivPar[p] >= n:
            continue
        e = tabPar[p][etuSuivPar[p]]
        etuSuivPar[p] += 1

        if affectEtu[e] is None:
            affectation[p].append(e)
            affectEtu[e] = p
            if len(affectation[p]) < cap[p]:
                parLibre.append(p)

        else:
            ancien = affectEtu[e]
            if inverse_tabEtu[e][p] < inverse_tabEtu[e][ancien]:
                affectation[ancien].remove(e)
                parLibre.append(ancien)
                affectation[p].append(e)
                affectEtu[e] = p
                if len(affectation[p]) < cap[p]:
                    parLibre.append(p)
            else:
                parLibre.append(p)

    return affectation,ite


#La complexité des 2 fonctions est en O(m x n)

#Q6

def verif_stap(affectation,tabEtu,tabPar,cap):
    instable = []
    affctEtu = [None]*len(tabEtu)

    for p in affectation:
        for e in affectation[p]:
            affctEtu[e] = p

    invEtu, _ = inverser(tabEtu)
    invPar, _ = inverser(tabPar)

    for e in range(len(tabEtu)):
        for p in range(len(tabPar)):
            if(affctEtu[e] is None or affctEtu[e] != p):
                if(invEtu[e][p]<invEtu[e][affctEtu[e]]):
                    if(len(affectation[p])<cap[p]):
                        instable.append((e,p))
                    else:
                        pire = affectation[p][0]
                        for etu in affectation[p]:
                            if(invPar[p][etu] > invPar[p][pire]):
                                pire = etu
                        if(invPar[p][e] < invPar[p][pire]):
                            instable.append((e,p))
    return instable
    

#Q7

def ale_etu(n, m=9):
    return [random.sample(range(m),m) for _ in range(n)]

def ale_par(n,m=9):
    return [random.sample(range(n),n) for _ in range(m)]

#Q8

def generer_capacites(n, m=9):
    base = n // m
    reste = n % m
    capacites = [base] * m
    for i in range(reste):
        capacites[i] += 1
    return capacites 

def question_8(nbT=10):
    Ltemps_etu = []
    Ltemps_par = []

    for n in range(200,2001,200):
        capacite = generer_capacites(n)
        temps_etu = 0
        temps_par = 0
        for j in range(nbT):
            ce = ale_etu(n)
            cp = ale_par(n)

            debut = time.time()
            gs_Etu(ce,cp,capacite)
            fin = time.time()
            temps_etu += fin - debut

            debut = time.time()
            gs_Par(ce,cp,capacite)
            fin = time.time()
            temps_par += fin - debut

        Ltemps_etu.append(temps_etu / nbT)
        Ltemps_par.append(temps_par / nbT)

    return Ltemps_etu, Ltemps_par

def trace_courbe(n, Ltemps_etu, Ltemps_par):
    plt.plot(n, Ltemps_etu, label="GS côté étudiants")
    plt.plot(n, Ltemps_par, label="GS côté parcours")
    plt.xlabel("n (nombre d'étudiants)")
    plt.ylabel("Temps moyen (s)")
    plt.title("Temps de calcul de Gale-Shapley")
    plt.legend()
    plt.show()

#Q10


def question_10(nbT=10):
    Ltemps_etu = []
    Ltemps_par = []

    for n in range(200,2001,200):
        capacite = generer_capacites(n)
        iteE = 0
        iteP = 0
        moy = 0
        for j in range(nbT):
            ce = ale_etu(n)
            cp = ale_par(n)

            z,a = gs_Etu(ce,cp,capacite)

            y,b = gs_Par(ce,cp,capacite)

            iteE += a
            iteP += b

        moy = iteE /nbT
        Ltemps_etu.append(moy)
        moy = iteP/nbT
        Ltemps_par.append(moy)

    return Ltemps_etu, Ltemps_par


#Q11 - Q12 - Q13 - Q14 (PLNE avec Gurobi)

import gurobipy as gp
from gurobipy import Model, GRB, quicksum

def liste_to_dict(aff_liste, m):
    d = {j: [] for j in range(m)}
    for i, j in enumerate(aff_liste):
        if j != -1:
            d[j].append(i)
    return d

def resoudre_affectation_max_min(pref_etu, pref_spe, capacites, k_limite=None):
    n = len(pref_etu)
    m = len(pref_spe)
    
    model = gp.Model("Affectation_MaxMin")
    model.setParam('OutputFlag', 0)
    # 1. Variables de décision
    x = model.addVars(n, m, vtype=GRB.BINARY, name="x")
    
    # Nouvelle variable : Utilité minimale parmi les étudiants
    u_min_var = model.addVar(vtype=GRB.INTEGER, name="u_min")

    # 2. Calcul des utilités (Borda)
    u_etu = [[0]*m for _ in range(n)]
    for i in range(n):
        for rang, j in enumerate(pref_etu[i]):
            u_etu[i][j] = (m - 1) - rang

    u_spe = [[0]*n for _ in range(m)]
    for j in range(m):
        for rang, i in enumerate(pref_spe[j]):
            u_spe[j][i] = (n - 1) - rang

    # 3. Contraintes standards
    model.addConstrs((x.sum(i, '*') == 1 for i in range(n)), name="Unicite")
    model.addConstrs((x.sum('*', j) == capacites[j] for j in range(m)), name="Capacite")

    # 4. Contraintes pour définir l'utilité minimale (Max-Min)
    # Pour chaque étudiant i, son utilité réelle doit être >= u_min_var
    for i in range(n):
        model.addConstr(
            gp.quicksum(x[i, j] * u_etu[i][j] for j in range(m)) >= u_min_var, 
            name=f"MinUtil_etu_{i}"
        )

    # 5. Fonction Objectif : Maximiser l'utilité minimale
    model.setObjective(u_min_var, GRB.MAXIMIZE)

    # 6. Optimisation
    model.optimize()

    # 7. Récupération des résultats
    if model.status == GRB.OPTIMAL:
        affectation = [-1] * n
        score_total_etu = 0
        score_total_spe = 0

        for i in range(n):
            for j in range(m):
                if x[i, j].X > 0.5:
                    affectation[i] = j
                    score_total_etu += u_etu[i][j]
                    score_total_spe += u_spe[j][i]
        
        moy_etu = score_total_etu / n
        moy_spe = score_total_spe / m
        
        util_min_etu_calculee = u_min_var.X
        
        return affectation, moy_etu, moy_spe, util_min_etu_calculee
    else:
        return None, None, None, None

def resoudre_affectation(pref_etu, pref_spe, capacites, k_limite=None):
    # n = 13 (étudiants), m = 10 (parcours)
    n = len(pref_etu)
    m = len(pref_spe)
    
    # 1. Création du modèle
    model = gp.Model("Affectation")
    model.setParam('OutputFlag', 0)
    # 2. Variables de décision : x[i,j] = 1 si l'étudiant i va dans le parcours j
    x = model.addVars(n, m, vtype=GRB.BINARY, name="x")

    # 3. Calcul des utilités (Scores de Borda)
    # Utilité etu[i][j] : quel score l'étudiant i donne au parcours j
    u_etu = [[0]*m for _ in range(n)]
    for i in range(n):
        for rang, j in enumerate(pref_etu[i]):
            u_etu[i][j] = (m - 1) - rang
            
    # Utilité spe[j][i] : quel score le parcours j donne à l'étudiant i
    u_spe = [[0]*n for _ in range(m)]
    for j in range(m):
        for rang, i in enumerate(pref_spe[j]):
            u_spe[j][i] = (n - 1) - rang

    # 4. Contraintes
    # Chaque étudiant est affecté à EXACTEMENT un parcours
    model.addConstrs((x.sum(i, '*') == 1 for i in range(n)), name="Unicite")
    
    # Chaque parcours respecte sa capacité maximale
    model.addConstrs((x.sum('*', j) == capacites[j] for j in range(m)), name="Capacite")

    # Question Q13/Q14 : Contrainte des k-premiers choix
    # Un étudiant i est dans ses k premiers choix si son utilité >= (m - k)
    if k_limite is not None:
        for i in range(n):
            model.addConstr(gp.quicksum(x[i, j] * u_etu[i][j] for j in range(m)) >= (m - k_limite))

    # 5. Fonction Objectif (Q12 : Maximiser la somme des utilités totales)
    obj = gp.quicksum(x[i, j] * (u_etu[i][j] + u_spe[j][i]) for i in range(n) for j in range(m))
    model.setObjective(obj, GRB.MAXIMIZE)

    # 6. Optimisation
    model.optimize()

    # 7. Récupération des résultats
    if model.status == GRB.OPTIMAL:
        affectation = [-1] * n
        score_total_etu = 0
        score_total_spe = 0

        for i in range(n):
            for j in range(m):
                if x[i, j].X > 0.5:
                    affectation[i] = j
                    score_total_etu += u_etu[i][j]
                    score_total_spe += u_spe[j][i]
        
        moy_etu = score_total_etu / n
        moy_spe = score_total_spe / m

        # Calcul des statistiques pour Q12 / Q15
        util_min_etu = min(u_etu[i][affectation[i]] for i in range(n))
        
        return affectation, moy_etu, moy_spe, util_min_etu
    else:
        return None, None, None, None

def question_14(pref_etu, pref_spe, capacites):
    print("--- Recherche du plus petit k (Question 14) ---")
    
    for k in range(1, 11):
        print(f"\nEssai pour k = {k}...")
        aff, moy_etu, moy_spe, k = resoudre_affectation(pref_etu, pref_spe, capacites, k_limite=k)
        
        if aff is not None:
            print(f"SUCCÈS : Mariage parfait trouvé pour k = {k} !")
            return aff, moy_etu, moy_spe, k
        else:
            print(f"ÉCHEC : Pas de solution pour k = {k}")




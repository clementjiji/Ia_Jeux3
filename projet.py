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
    etuLibre = [n for n in range(len(tabEtu))]
    parSuivEtu = [0] * len(tabEtu)
    inverse_tabPar,pires = inverser(tabPar)
    affectation = {}
    for j in range(len(tabPar)):
        affectation[j] = []
    pires = {}

    while len(etuLibre) > 0:
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

    return affectation

#Q4

def gs_Par(tabEtu,tabPar,cap):
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
        p = parLibre.pop()
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

    return affectation


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


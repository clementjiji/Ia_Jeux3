import exemple # Pour pouvoir utiliser les methodes de exemple.py
import projet


etu = projet.prefetu('./PrefEtu.txt')
for i in range(len(etu)):
    for j in range(len(etu[i])):
        print(etu[i][j]," ",end="")
    print()

print()

cap,parc = projet.prefpar('./PrefSpe.txt')
for i in range(len(parc)):
    for j in range(len(parc[i])):
        print(parc[i][j]," ",end="")
    print()

print()

print("---coté étudiant---")
print()

affectation1,ite1 = projet.gs_Etu(etu,parc,cap)
for i in range(len(affectation1)):
    for j in range(len(affectation1[i])):
        print(affectation1[i][j]," ",end="")
    print()

print("---coté parcours---")
print()

affectation2,ite2 = projet.gs_Par(etu,parc,cap)
for i in range(len(affectation2)):
    for j in range(len(affectation2[i])):
        print(affectation2[i][j]," ",end="")
    print()

print()
print("---verif_strap---")

print(projet.verif_stap(affectation1, etu, parc, cap))
print(projet.verif_stap(affectation2, etu, parc, cap))

print("---Q8---")
print()

Ltemps_etu, Ltemps_par = projet.question_8(10)

valeurs_n = list(range(200,2001,200))
projet.trace_courbe(valeurs_n, Ltemps_etu, Ltemps_par)

print('---Q10---')
print()

ite_etu,ite_par = projet.question_10(30)

projet.trace_courbe(valeurs_n,ite_etu,ite_par)


print("---Q11 (max-min Borda)---")

aff_min, m_e_min, m_s_min, u_min =  projet.resoudre_affectation_max_min(etu, parc, cap)

aff_max, m_e_max, m_s_max, u_min_max = projet.resoudre_affectation(etu, parc, cap)

aff_k, m_e_k, m_s_k, k_min = projet.question_14(etu, parc, cap)

m_par = len(parc)

print("\n\nResoudre Affectation Q11")
print(f"Utilité moy Etu : {m_e_min}\nUtilité moy Spe : {m_s_min}\n Utilité min : {u_min}\n Affectation : {aff_min}")
print(f'Mariages instables : {projet.verif_stap(projet.liste_to_dict(aff_min, m_par), etu, parc, cap)}')

print("\n\nResoudre Affectation Q12")
print(f"Utilité moy Etu : {m_e_max}\nUtilité moy Spe : {m_s_max}\n Utilité min : {u_min_max}\n Affectation : {aff_max}")
print(f'Mariages instables : {projet.verif_stap(projet.liste_to_dict(aff_max, m_par), etu, parc, cap)}')

print("\n\nResoudre Affectation Q14")
print(f"Utilité moy Etu : {m_e_k}\nUtilité moy Spe : {m_s_k}\n K min : {u_min}\n Affectation : {aff_k}")
print(f'Mariages instables : {projet.verif_stap(projet.liste_to_dict(aff_k, m_par), etu, parc, cap)}')

print("\n\n---Q15 (comparaison des solutions)---")
projet.question_15(etu, parc, cap)
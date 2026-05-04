import exemple # Pour pouvoir utiliser les methodes de exemple.py
import projet


etu = projet.prefetu('/home/clmentjiang/githubPerso/Ia_Jeux3/PrefEtu.txt')
for i in range(len(etu)):
    for j in range(len(etu[i])):
        print(etu[i][j]," ",end="")
    print()

print()

cap,parc = projet.prefpar('/home/clmentjiang/githubPerso/Ia_Jeux3/PrefSpe.txt')
for i in range(len(parc)):
    for j in range(len(parc[i])):
        print(parc[i][j]," ",end="")
    print()

print()

print("---coté étudiant---")
print()

affectation1 = projet.gs_Etu(etu,parc,cap)
for i in range(len(affectation1)):
    for j in range(len(affectation1[i])):
        print(affectation1[i][j]," ",end="")
    print()

print("---coté parcours---")
print()

affectation2 = projet.gs_Par(etu,parc,cap)
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
aff11, u_min = projet.question_11(etu, parc, cap)
print("Affectation:", aff11)
print("Utilité minimale:", u_min)

print("---Q12 (max somme utilités)---")
aff12 = projet.question_12(etu, parc, cap)
print("Affectation:", aff12)
bE = projet.borda_etu(etu)
bP = projet.borda_par(parc, len(etu))
util_etu, util_par = projet.utilites(aff12, bE, bP)
print("Utilité moyenne (étu):", sum(util_etu)/len(util_etu))
print("Utilité minimale (étu):", min(util_etu))
print("Utilité totale parcours:", util_par)

print("---Q14 (plus petit k pour mariage parfait)---")
k, aff14 = projet.question_14(etu, parc, cap)
print(f"Plus petit k = {k}")
print("Affectation:", aff14)

print()
print("---Q15 (comparaison des solutions)---")
print()

def stats(nom, aff):
    instables = projet.verif_stap(aff, etu, parc, cap)
    util_e, _ = projet.utilites(aff, bE, bP)
    util_moy = sum(util_e) / len(util_e)
    util_min = min(util_e)
    stable = "Oui" if len(instables) == 0 else "Non"
    print(f"{nom:25s} | stable: {stable:3s} | # instables: {len(instables):3d} | util moy: {util_moy:5.2f} | util min: {util_min}")

stats("GS coté étudiants", affectation1)
stats("GS coté parcours", affectation2)
stats("Q11 (max-min Borda)", aff11)
stats("Q12 (max somme)", aff12)
stats(f"Q14 (k={k} premiers)", aff14)
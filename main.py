import exemple # Pour pouvoir utiliser les methodes de exemple.py
import projet


etu = projet.prefetu(r'C:\Users\clemo\Desktop\Github\Fwdprojet\PrefEtu.txt')
for i in range(len(etu)):
    for j in range(len(etu[i])):
        print(etu[i][j]," ",end="")
    print()

print()

cap,parc = projet.prefpar(r'C:\Users\clemo\Desktop\Github\Fwdprojet\PrefSpe.txt')
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
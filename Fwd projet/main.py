import exemple # Pour pouvoir utiliser les methodes de exemple.py
import projet


a = projet.prefetu('/users/Etu4/21202334/Documents/ia/PrefEtu.txt')
for i in range(len(a)):
    for j in range(len(a[i])):
        print(a[i][j]," ",end="")
    print()


x,b = projet.prefpar('/users/Etu4/21202334/Documents/ia/PrefSpe.txt')
for i in range(len(b)):
    for j in range(len(b[i])):
        print(b[i][j]," ",end="")
    print()
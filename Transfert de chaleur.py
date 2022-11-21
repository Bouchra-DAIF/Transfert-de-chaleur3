print("Transfert de chaleur")
T1=input("Entrez la température initiale: ")
T2=input("Entrez la température finale: ")
e1=input("Entrez la première épaisseur: ")
e2=input("Entrez dans la deuxième épaisseur: ")
L=input("Entrez la largeur L: ")
l1=input("Entrez la largeur de la première Brique: ")
l2=input("Entrez la largeur du vide: ")
Lmb=input("Etrez lambda de Brique: ")
Lmv=input("Entrez lambda de vide: ")
try:
    T1=float(T1)
    T2=float(T2)
    e1=float(e1)
    e2=float(e2)
    L=float(L)
    l1=float(l1)
    l2=float(l2)
    Lmb=float(Lmb)
    Lmv=float(Lmv)

    Ra=(e2)/(Lmb+L+l1)
    print(Ra)
    Rc=Ra
    print(Rc)
    Rb=(e2)/(Lmv+L+l1)
    print(Rb)
    Req=1/((1/Ra)+(1/Rb)+(1/Rc))
    print(Req)
    l=l1+l2*2
    R1=(e1)/(Lmv+L+l)
    print(R1)
    R2=R1
    print(R2)
    R=R1+Req+R2
    print(R)
    Fl=(T1-T2)/R
    print("le flux est", Fl)
except:
    print("erreur")


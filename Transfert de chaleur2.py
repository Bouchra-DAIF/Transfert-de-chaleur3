import matplotlib.pyplot as plt

n = int(input("Enter number of elements : "))
lambdas = []
epaisseur = []
temp = []
for i in range(n):
    lambdas.append(float(input("Enter lambda " + str(i) + " : ")))
    epaisseur.append(float(input("Enter epaisseur " + str(i) + " : ")))
    t1 = float(input("Temperature 1 : "))
    t2 = float(input("Temperature 2 : "))
    temp.append([t1, t2])

x_axis = []
y_axis = []
for i in range(n):
    if len(x_axis) == 0:
        a = 0
    else:
        a = x_axis[len(x_axis)-1]
    x_axis.append(a)
    y_axis.append(temp[i][0])
    x_axis.append(a + epaisseur[i])
    y_axis.append(temp[i][1])

plt.plot(x_axis, y_axis)
plt.plot(x_axis, y_axis, "o")
for i in x_axis:
    plt.axvline(x = i, color = 'g')
plt.axis([0, int(sum(epaisseur)) + 1, 0, max(max(temp)) + 5])
plt.ylabel('Temperature')
plt.show()

print("flux")
S=input("Entrez la surface: ")
T1=input("Entrez la température initiale: ")
T2=input("Entrez la température finale: ")
e1=input("Entrez la première épaisseur: ")
e2=input("Entrez dans la deuxième épaisseur: ")
Lam1=input("Etrez lambda 1: ")
Lam2=input("Entrez lambda 2: ")
try:
    T1=float(T1)
    T2=float(T2)
    e1=float(e1)
    e2=float(e2)
    Lam1=float(Lam1)
    Lam2=float(Lam2)
    S = float(S)
    R1 = (e1) / (Lam1 * S)
    print("La première résistance est", R1)
    R2 = (e2) / (Lam2 * S)
    print("La deuxiéme résistance est", R2)
    Fl = (t1 - t2) / R1 + R2
    print("le flux est", Fl)
except:
    print("erreur")

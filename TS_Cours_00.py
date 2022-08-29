# TS_Cours_01
# Rappel - Suite et Algorithme

def Solution_Second_Degre(a,b,c):
# cherche les solutions d'1 trinome du 2° degré
# en fonction de la valeur de delta

  delta =b**2 - 4*a*c
  print (" Delta =",delta )
  if delta <0:
    print ("Pas de solutions ")
  if delta ==0:
    print ("Une solution ")
    x=-b/2*a
    print ("X=",x)
  if delta >0:
    print (" Deux solutions ")
    x1 = (-b - sqrt(delta)) / (2*a)
    x2 = (-b + sqrt(delta)) / (2*a)
    print ("X1=",x1)
    print ("X2=",x2)
 
def Rappel_Boucle_Tant_Que(p):
# p étant un entier positif
# permet de trouver le premier n tel que 
# 1 + 2 + ... + n > 10**p
# au moyen de la suite U

  n,U = 0,0
  while U <= 10**p:
    n = n+1
    U = U+n
  print ("N=",n)
  
def calcul_de_Factorielle(n):
# calcule factorielle n grâce à une boucle for
  k = 1
  for i in range (1, n+1) :
    k = k*i
  print (n,"! = ",k)  

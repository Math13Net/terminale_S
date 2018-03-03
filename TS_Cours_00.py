# TS_Cours_00
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

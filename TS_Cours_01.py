# TS_Cours_01
# Chapitre 1 : Raisonnement par récurrence - Limite d'une suite

def precision_valeur(limite,precision):
# U_0 = 0.1 et U_{n+1} = 2*U_n(1-U_n)
# Algorithme de précision ayant pour paramètre la limite et la précision
# trouve le rang n tq abs(U_n-limite) < precision
  U = 0.1
  n = 0
  while abs(U - limite) >= precision :
    U = 2*U*(1 -U)
    n += 1
  print ("n = ",n)
  print("U_n = ",U)
  print (" |",U," - ",limite," | = ",abs(U -0.5) )


def depassement_valeur(A):
# U_0 = 2 et U_{n+1} = 4/3*U_n + 1
# Algorithme de dépassement d'1 valeur A donnée
# trouver le rang n tel que U_n > A

  U = -2
  n = 0
  while U <= A:
    U = 4/3* U+1
    n +=1
  print ("N = ",n)
  print ("U = ",U)

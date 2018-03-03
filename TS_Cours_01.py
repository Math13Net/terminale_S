# TS_Cours_01
# Chapitre 1 : Raisonnement par récurrence - Limite d'une suite

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

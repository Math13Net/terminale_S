# TS_Cours_01
# Chapitre 11 : Intégration

-------------------------------------------------------------------------------------------
# intégration : méthode des rectangles et des trapèzes
# f(x) = x^2 sur [0,5]

from math import *
import numpy as np

# definition de la fonction
def f(x):
  return x**2

# bornes intégration
a, b = 0, 5

# Méthode des Rectangles à Gauche
def rectangle_gauche(a,b,n,f):
  x=np.linspace(a, b, n+1)[:-1]
  return((b-a)/n*np.sum(f(x)))

# Méthode des Rectangles à Droite
def rectangle_droite(a,b,n,f):
  x=np.linspace(a, b, n+1)[1:]
  return((b-a)/n*np.sum(f(x)))
  
# Méthode des Trapèzes
def trapeze(a,b,n,f):
  x=np.linspace(a,b,n+1)
  return ((b-a)/n*(1/2*f(x[0])+np.sum(f(x[1:n]))+1/2*f(x[n])))

# affichage des résultats
print('-'*60)
print('{0:>10s} | {1:^12s} | {2:^14s} | {3:^15s} '.format('n', 'Rect_Gauche', 'Rect_Droite', 'Trapèze'))
print('-'*60)
for i in range(1, 7):
  n = 10**i
  rg = rectangle_gauche(a,b,n,f)
  rd = rectangle_droite(a,b,n,f)
  t = trapeze(a,b,n,f)
  print('{0:10d} | {1:11f}  | {2:13f}  | {3:14f}'.format(n,rg,rd,t))
print('-'*60)
--------------------------------------------------------------------------------------------


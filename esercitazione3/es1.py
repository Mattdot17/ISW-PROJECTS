"""
data una lista di numeri, restituire una nuova
lista i cui elementi sono il quadrato del numero[i] se
questo è minore di 50, il cubo del numero[i] se è maggiore
di 50.
"""
import random

'''
tupl = ('c', 'c', 'c', 'c', 'cggg', 6, 'ciao')
print(tupl)
print(tupl.count('c'))

seq = ['aljjjha', 'beta', 'gamma', 'delta']
for gigi in seq:
    if len(gigi) == 4:
        continue #procedi all'elemento successivo
    print('Sto controllando', gigi)
    if gigi == 'gamma':
        print('Elemento trovato!')
        break #elemento trovato, interrompi il ciclo
'''
lista = []
for i in range(10):
    lista.append(random.randint(1,100))
print("Lista di partenza", lista)

quadrato = [x ** 2 for x in lista if x < 50]
print("quadrato numeri minori di 50", quadrato)

cubo = [x**3 for x in lista if x>50]
print("cubo numeri maggiori di 50", cubo)
